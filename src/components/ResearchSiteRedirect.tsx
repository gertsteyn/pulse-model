import React from 'react';
import Head from '@docusaurus/Head';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import Heading from '@theme/Heading';
import Layout from '@theme/Layout';

type ResearchSite = {
  label: string;
  routeBasePath: string;
  firstDocId: string;
};

type Props = {
  site: ResearchSite;
};

function sitePath(site: ResearchSite): string {
  return site.routeBasePath === '/' ? '/' : `/${site.routeBasePath}`;
}

function targetPathForSite(site: ResearchSite): string {
  if (site.firstDocId === 'index') {
    return sitePath(site);
  }

  return `${sitePath(site).replace(/\/$/, '')}/${site.firstDocId}`;
}

export default function ResearchSiteRedirect({site}: Props): React.ReactNode {
  const targetPath = targetPathForSite(site);
  const targetUrl = useBaseUrl(targetPath);

  return (
    <Layout title={site.label} description={`${site.label} research documents`}>
      <Head>
        <meta httpEquiv="refresh" content={`0; url=${targetUrl}`} />
      </Head>
      <main className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset-2">
            <div className="theme-doc-markdown markdown">
              <Heading as="h1">{site.label}</Heading>
              <p>
                <Link to={targetPath}>Open {site.label}</Link>
              </p>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
