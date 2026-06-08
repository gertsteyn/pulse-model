import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
import {themes as prismThemes} from 'prism-react-renderer';
import type {Config, LoadContext, Plugin} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math';

type ResearchSite = {
  id: string;
  dir: string;
  label: string;
  routeBasePath: string;
  firstDocId: string;
};

type SidebarItem = {
  type?: string;
  id?: string;
  label?: string;
  items?: SidebarItem[];
};

type SidebarGeneratorArgs = {
  defaultSidebarItemsGenerator: (args: SidebarGeneratorArgs) => SidebarItem[] | Promise<SidebarItem[]>;
};

const orgName = process.env.ORG_NAME || 'gertsteyn';
const projectName = process.env.PROJECT_NAME || 'pulse-model';
const siteUrlEnv = process.env.SITE_URL || `https://${orgName}.github.io/${projectName}`;
const repoRoot = process.cwd();
const primaryResearchDir = 'pulse_model';

const supportDirs = new Set([
  'build',
  'node_modules',
  'src',
  'static',
]);

function parseUrl(fullUrl: string): {origin: string; baseUrl: string} {
  try {
    const parsed = new URL(fullUrl);
    const baseUrl =
      parsed.pathname === '/'
        ? `/${projectName}/`
        : parsed.pathname.endsWith('/')
          ? parsed.pathname
          : `${parsed.pathname}/`;
    return {origin: parsed.origin, baseUrl};
  } catch {
    return {origin: `https://${orgName}.github.io`, baseUrl: `/${projectName}/`};
  }
}

function toKebab(input: string): string {
  return input
    .replace(/_/g, '-')
    .replace(/([a-z0-9])([A-Z])/g, '$1-$2')
    .replace(/[^a-zA-Z0-9-]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .toLowerCase();
}

function toTitle(input: string): string {
  return input
    .split(/[_-]+/)
    .filter(Boolean)
    .map((word) => `${word.charAt(0).toUpperCase()}${word.slice(1)}`)
    .join(' ');
}

function markdownFiles(dir: string): string[] {
  const files: string[] = [];

  function walk(currentDir: string): void {
    for (const entry of fs.readdirSync(currentDir, {withFileTypes: true})) {
      const fullPath = path.join(currentDir, entry.name);
      if (entry.isDirectory()) {
        walk(fullPath);
      } else if (entry.isFile() && /\.mdx?$/.test(entry.name)) {
        files.push(path.relative(dir, fullPath));
      }
    }
  }

  walk(dir);
  return files.sort();
}

function firstDocId(dir: string, files: string[]): string {
  const rootFiles = files.filter((file) => !file.includes(path.sep));
  const preferred =
    rootFiles.find((file) => path.basename(file, path.extname(file)) === 'index') ||
    rootFiles.find((file) => path.basename(file, path.extname(file)) === dir) ||
    rootFiles[0] ||
    files[0];

  return preferred.replace(/\.mdx?$/, '').split(path.sep).join('/');
}

function routeBasePathForDir(dir: string): string {
  return dir === primaryResearchDir ? '/' : toKebab(dir);
}

function siteLink(site: ResearchSite): string {
  return site.routeBasePath === '/' ? '/' : `/${site.routeBasePath}/`;
}

function discoverResearchSites(): ResearchSite[] {
  return fs
    .readdirSync(repoRoot, {withFileTypes: true})
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .filter((dir) => !dir.startsWith('.') && !supportDirs.has(dir))
    .map((dir) => ({dir, files: markdownFiles(path.join(repoRoot, dir))}))
    .filter(({files}) => files.length > 0)
    .map(({dir, files}) => ({
      id: toKebab(dir),
      dir,
      label: toTitle(dir),
      routeBasePath: routeBasePathForDir(dir),
      firstDocId: firstDocId(dir, files),
    }))
    .sort((a, b) => a.label.localeCompare(b.label));
}

function hasGitCommits(): boolean {
  try {
    execFileSync('git', ['rev-parse', '--verify', 'HEAD'], {
      cwd: repoRoot,
      stdio: 'ignore',
    });
    return true;
  } catch {
    return false;
  }
}

function normalizeRoute(parts: string[]): string {
  const route = parts
    .join('/')
    .replace(/\/+/g, '/')
    .replace(/\/$/g, '');

  return route.startsWith('/') ? route : `/${route}`;
}

function researchSiteIndexPlugin({baseUrl}: LoadContext): Plugin {
  return {
    name: 'science-research-site-indexes',
    contentLoaded({actions: {addRoute}}) {
      for (const site of researchSites) {
        if (site.firstDocId === 'index') {
          continue;
        }

        addRoute({
          path: normalizeRoute([baseUrl, site.routeBasePath]),
          component: '@site/src/components/ResearchSiteRedirect',
          exact: true,
          props: {
            site,
          },
        });
      }
    },
  };
}

async function rootDocsFirstSidebarItemsGenerator(args: SidebarGeneratorArgs): Promise<SidebarItem[]> {
  const items = normalizeSidebarItems(await args.defaultSidebarItemsGenerator(args));
  const rootDocs = items.filter((item) => item.type === 'doc');
  const otherItems = items.filter((item) => item.type !== 'doc');

  return [...rootDocs, ...otherItems];
}

function normalizeSidebarItems(items: SidebarItem[]): SidebarItem[] {
  return items.flatMap((item) => {
    const label = item.label || '';
    const normalizedLabel = label.toLowerCase();

    if (item.type === 'doc') {
      const id = item.id || '';
      if (
        hiddenDocIds.has(id) ||
        id.startsWith('appendix/geometry_action_') ||
        id.startsWith('appendix/geometry_phase_functional_') ||
        id.startsWith('appendix/h2_') ||
        id.startsWith('appendix/h6_') ||
        normalizedLabel.includes('compatibility') ||
        normalizedLabel === 'migration map'
      ) {
        return [];
      }

      return [item];
    }

    if (item.type !== 'category') {
      return [item];
    }

    return [
      {
        ...item,
        label: normalizedLabel === 'appendix' ? 'Appendix' : item.label,
        items: item.items ? normalizeSidebarItems(item.items) : item.items,
      },
    ];
  });
}

const researchSites = discoverResearchSites();
const {origin: siteUrl, baseUrl} = parseUrl(siteUrlEnv);
const showLastUpdateTime = hasGitCommits();

const hiddenDocIds = new Set([
  'documentation_migration_map',
  'h2_acceptance_report',
  'known_physics_validation_report',
  'proof_sequence',
  'promising_tweaks',
  'pulse_model_formalization',
]);

const config: Config = {
  title: 'Science Research',
  tagline: 'Research notes and formalizations',
  favicon: 'img/favicon.svg',

  themes: ['@docusaurus/theme-mermaid'],

  url: siteUrl,
  baseUrl,
  organizationName: orgName,
  projectName,
  trailingSlash: false,

  onBrokenLinks: 'warn',

  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  customFields: {
    researchSites,
  },

  plugins: [
    ...researchSites.map((site) => [
      '@docusaurus/plugin-content-docs',
      {
        id: site.id,
        path: site.dir,
        routeBasePath: site.routeBasePath,
        sidebarPath: './sidebars.ts',
        sidebarItemsGenerator: rootDocsFirstSidebarItemsGenerator,
        remarkPlugins: [remarkMath],
        rehypePlugins: [rehypeKatex],
        showLastUpdateTime,
      },
    ]),
    researchSiteIndexPlugin,
  ],

  presets: [
    [
      'classic',
      {
        docs: false,
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    colorMode: {
      defaultMode: 'dark',
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Science',
      logo: {
        alt: 'Science Logo',
        src: 'img/logo.svg',
      },
      items: [
        ...researchSites.map((site) => ({
          to: siteLink(site),
          position: 'left' as const,
          label: site.label,
        })),
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Research',
          items: researchSites.map((site) => ({
            label: site.label,
            to: siteLink(site),
          })),
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} <a href="https://senseware.com">Senseware Labs</a>.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'json', 'toml', 'go'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
