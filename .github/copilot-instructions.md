# Simply Track Time Hugo Blog

Simply Track Time is a static blog built with Hugo v0.150.0+ using the CleanWhite theme. The blog contains articles about time management, productivity, and life balance. 

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

Bootstrap and build the blog:
- `git submodule update --init --recursive` -- initializes theme submodules (takes 10-30 seconds)
- Install Hugo v0.150.0 or later:
  ```bash
  wget -O hugo.deb https://github.com/gohugoio/hugo/releases/download/v0.150.0/hugo_extended_0.150.0_linux-amd64.deb
  sudo dpkg -i hugo.deb
  ```
- `hugo --gc --minify` -- builds the site (takes ~200ms, NEVER CANCEL, use 30+ second timeout)
- `hugo version` -- verify Hugo is v0.150.0+ (required for theme compatibility)

Run the development server:
- `hugo server --bind 0.0.0.0 --port 1313` -- starts dev server at http://localhost:1313
- Server starts in ~200ms and provides live reload functionality
- Press Ctrl+C to stop the server

## Validation

Always manually validate changes by running the development server and accessing the blog:
- Start server: `hugo server --bind 0.0.0.0 --port 1313`
- Test homepage: `curl -s http://localhost:1313/ | head -20`
- Verify build: `hugo --gc --minify` (must complete without errors)
- ALWAYS test that new content appears correctly on the homepage and individual post pages
- Take screenshots when making content or theme changes to verify visual layout

## Content Management

Create new blog posts:
- `hugo new content/post/YYYY-MM-DD-post-title.md` -- creates new post with archetype template
- Posts use CleanWhite theme archetype with fields: title, subtitle, description, date, author, image, tags, categories
- Set `draft: false` to publish posts
- Posts are in `content/post/` directory with date-prefixed filenames

Check content status:
- `hugo list drafts` -- shows all draft posts
- Content structure: `content/post/` (blog posts), `content/about/` (about page)
- Static assets: `static/img/` (images and favicons)

## Build Process

Hugo builds the site from source to `public/` directory:
- **Build time**: ~200ms (very fast, no timeout concerns needed)
- **Required Hugo version**: v0.150.0+ (theme uses `try` function not available in older versions)
- **Dependencies**: Git submodules for themes must be initialized before first build
- **Output**: Static HTML files in `public/` directory (excluded from git via .gitignore)

No Node.js, package.json, tests, or linting tools are used in this project.

## Theme Information

Uses CleanWhite Hugo theme (git submodule):
- Theme path: `themes/hugo-theme-cleanwhite/`  
- Multiple themes available but only CleanWhite is configured in `hugo.toml`
- Theme requires Hugo v0.150.0+ for modern template functions
- Custom archetype provides structured post template with metadata fields

## Common Issues

Hugo version compatibility:
- If build fails with "function 'try' not defined", upgrade Hugo to v0.150.0+
- Old Hugo versions (v0.111.3 and earlier) cannot build this site due to theme requirements

Git submodule issues:
- If themes are missing, run: `git submodule update --init --recursive`
- Theme files should exist in `themes/hugo-theme-cleanwhite/layouts/`

## Repository Structure

```
.
├── hugo.toml          # Hugo configuration
├── content/           # Content source files
│   ├── about/         # About page
│   └── post/          # Blog posts (YYYY-MM-DD-title.md format)
├── static/            # Static assets (images, etc.)
├── themes/            # Git submodules for Hugo themes
├── archetypes/        # Content templates
└── public/            # Generated site (excluded from git)
```

## CI/CD

GitHub Actions workflow (`.github/workflows/hugo.yml`):
- Deploys to GitHub Pages on push to master branch
- Uses Hugo v0.111.3 (may need upgrading to match local requirements)
- Builds with `--gc --minify` flags for production optimization