import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Heading from '@theme/Heading';
import Layout from '@theme/Layout';

type ResearchSite = {
  dir: string;
  label: string;
  routeBasePath: string;
};

export default function Home(): React.ReactNode {
  const {siteConfig} = useDocusaurusContext();
  const researchSites = (siteConfig.customFields?.researchSites ?? []) as ResearchSite[];

  return (
    <Layout title="Science Research" description="Research documents published from this repository">
      <main className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset-2">
            <div className="theme-doc-markdown markdown">
              <Heading as="h1">Science Research</Heading>
              <p>Research documents published from this repository.</p>
              <ul>
                {researchSites.map((site) => (
                  <li key={site.dir}>
                    <Link to={`/${site.routeBasePath}/`}>{site.label}</Link>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
