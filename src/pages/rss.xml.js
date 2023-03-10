import rss from '@astrojs/rss';
import { SITE_TITLE, SITE_DESCRIPTION } from '../config';

const posts = Object.values(import.meta.glob('./blog/**/*.{md,mdx}', { eager: true }));
// const posts = Astro.glob('./blog/**/*.{md,mdx}');

export const get = async () =>
	rss({
		title: SITE_TITLE,
		description: SITE_DESCRIPTION,
		site: import.meta.env.SITE,
		items: posts.map(md => ({
			title: md.frontmatter.title,
			description: md.frontmatter.description,
			pubDate: md.frontmatter.published,
			link: md.url,
		}))
	});

