# Simply Track Time Blog

[![Deploy Hugo site to Pages](https://github.com/simplytracktime/blog/actions/workflows/hugo.yml/badge.svg)](https://github.com/simplytracktime/blog/actions/workflows/hugo.yml)

A static blog built with Hugo focusing on time management, productivity, and life balance. The blog explores effective ways to track and optimize time investment for better personal and professional outcomes.

## 🌐 Live Site

Visit the blog at: [https://blog.simplytracktime.com/](https://blog.simplytracktime.com/)

## 📖 About

Simply Track Time is a search to come up with a better way to account for time. As Shakespeare wrote, "Time is the great leveller" - we each get approximately the same number of years. This blog investigates ways to achieve the best return on time invested through:

- Time management strategies and techniques
- Productivity methodologies (Getting Things Done, Pomodoro, etc.)
- Planning and goal-setting approaches
- Work-life balance insights
- Practical tools and applications

## 🛠 Technology Stack

- **Hugo**: v0.150.0+ (Static Site Generator)
- **Theme**: CleanWhite Hugo Theme
- **Deployment**: GitHub Pages via GitHub Actions
- **Content Management**: Markdown files with YAML frontmatter

## 🚀 Quick Start

### Prerequisites

- Git
- Hugo v0.150.0 or later (extended version required)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/simplytracktime/blog.git
   cd blog
   ```

2. **Initialize theme submodules:**
   ```bash
   git submodule update --init --recursive
   ```

3. **Install Hugo (if not already installed):**
   ```bash
   # Linux/Ubuntu
   wget -O hugo.deb https://github.com/gohugoio/hugo/releases/download/v0.150.0/hugo_extended_0.150.0_linux-amd64.deb
   sudo dpkg -i hugo.deb
   
   # macOS
   brew install hugo
   
   # Windows
   choco install hugo-extended
   ```

4. **Verify Hugo installation:**
   ```bash
   hugo version
   ```

5. **Build the site:**
   ```bash
   hugo --gc --minify
   ```

6. **Run development server:**
   ```bash
   hugo server --bind 0.0.0.0 --port 1313
   ```

   The site will be available at `http://localhost:1313`

## 📝 Content Management

### Creating New Posts

Create new blog posts using Hugo's content creation command:

```bash
hugo new content/post/YYYY-MM-DD-post-title.md
```

This uses the archetype template with the following frontmatter structure:

```yaml
---
title: 'Your Post Title'
date: 2023-12-01T21:39:10+12:00
draft: false
---
```

### Content Structure

```
content/
├── about/           # About page
└── post/           # Blog posts (date-prefixed filenames)
    ├── 2023-02-14-routine.md
    ├── 2023-03-12-getting-things-done.md
    └── ...
```

### Publishing Posts

- Set `draft: false` in the frontmatter to publish posts
- Posts are automatically deployed when pushed to the `main` branch
- Use the YYYY-MM-DD prefix format for consistent organization

## 🎨 Theme Configuration

The blog uses the CleanWhite theme configured in `hugo.toml`:

```toml
theme = 'hugo-theme-cleanwhite'

[params]
  header_image = "img/river.png"
  site_logo = "img/logo.jpg" 
  avatar = "img/logo.jpg"
  description = "Investigating ways to achieve the best return on time invested."
```

## 🔧 Development

### Available Commands

```bash
# Build for production
hugo --gc --minify

# Development server with live reload
hugo server --bind 0.0.0.0 --port 1313

# Check version
hugo version

# List draft posts
hugo list drafts

# Create new content
hugo new content/post/YYYY-MM-DD-title.md
```

### Build Performance

- **Build time**: ~123ms (very fast)
- **Pages generated**: 57 pages
- **Static files**: 65 files
- **Themes available**: 4 (ananke, hugo-book, hugo-theme-cleanwhite, m10c)

## 🚀 Deployment

The site automatically deploys to GitHub Pages using GitHub Actions when changes are pushed to the `main` branch. The workflow:

1. Installs Hugo v0.150.0
2. Checks out code with submodules
3. Builds the site with `hugo --gc --minify`
4. Deploys to GitHub Pages

## 📁 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── hugo.yml          # GitHub Actions deployment
├── archetypes/
│   └── default.md            # Content template
├── bin/
│   └── rename.py             # Utility script for renaming posts
├── content/
│   ├── about/                # About page
│   └── post/                 # Blog posts (45+ articles)
├── static/
│   └── img/                  # Images and assets
├── themes/                   # Hugo themes (git submodules)
│   ├── ananke/
│   ├── hugo-book/
│   ├── hugo-theme-cleanwhite/
│   └── m10c/
├── hugo.toml                 # Hugo configuration
├── go.mod                    # Go module file
└── public/                   # Generated site (excluded from git)
```

## 🛠 Utilities

### Post Renaming Script

The `bin/rename.py` script helps standardize post filenames by extracting dates and titles from frontmatter:

```bash
cd bin/
python3 rename.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-post`)
3. Add your content or improvements
4. Commit your changes (`git commit -am 'Add new post about productivity'`)
5. Push to the branch (`git push origin feature/new-post`)
6. Create a Pull Request

## 📄 License

This project is open source. Please respect copyright for individual blog posts and content.

## 🔗 Links

- **Live Site**: [https://blog.simplytracktime.com/](https://blog.simplytracktime.com/)
- **Hugo Documentation**: [https://gohugo.io/documentation/](https://gohugo.io/documentation/)
- **CleanWhite Theme**: [https://github.com/zhaohuabing/hugo-theme-cleanwhite](https://github.com/zhaohuabing/hugo-theme-cleanwhite)

---

*"Time is the great leveller" - investigating better ways to make the most of our shared resource.*