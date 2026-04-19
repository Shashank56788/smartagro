# GitHub Pages Deployment Guide

This guide will help you deploy the Smart Agriculture AI System website to GitHub Pages.

## 📁 File Structure for GitHub Pages

```
your-repo.github.io/
├── index.html          # Home page with project overview
├── dashboard.html      # Interactive sensor dashboard
├── style.css           # Shared styles for all pages
├── script.js           # JavaScript for interactions
└── README.md           # Project documentation
```

## 🚀 Deployment Steps

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon and select "New repository"
3. Name your repository: `username.github.io` (replace `username` with your GitHub username)
   - Example: `johndoe.github.io`
4. Make it **Public**
5. Check "Add a README file"
6. Click "Create repository"

### Step 2: Upload Files

**Option A: Using GitHub Web Interface**

1. On your repository page, click "Add file" → "Upload files"
2. Drag and drop these files:
   - `index.html`
   - `dashboard.html`
   - `style.css`
   - `script.js`
3. Add a commit message: "Initial commit - Smart Agriculture AI website"
4. Click "Commit changes"

**Option B: Using Git Command Line**

```bash
# Navigate to your project folder
cd path/to/your/project

# Initialize git repository
git init

# Add all files
git add index.html dashboard.html style.css script.js

# Commit files
git commit -m "Initial commit - Smart Agriculture AI website"

# Add remote repository
git remote add origin https://github.com/username/username.github.io.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" (gear icon)
3. Scroll down to "Pages" in the left sidebar
4. Under "Source", select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click "Save"

### Step 4: Wait for Deployment

1. GitHub will build your site (takes 1-5 minutes)
2. You'll see a message: "Your site is published at https://username.github.io"
3. Click the link to view your website!

## 🌐 Your Website URLs

After deployment, your site will be available at:

- **Home Page**: `https://username.github.io/`
- **Dashboard**: `https://username.github.io/dashboard.html`

## 📝 Customization Options

### Update Site Title and Meta Tags

Edit `index.html` and `dashboard.html`:

```html
<head>
    <title>Your Custom Title - Smart Agriculture AI</title>
    <meta name="description" content="Your custom description here">
    <meta name="keywords" content="agriculture, AI, IoT, farming">
</head>
```

### Change Colors

Edit `style.css` at the top (CSS Variables):

```css
:root {
    --primary-color: #667eea;    /* Change to your brand color */
    --secondary-color: #764ba2;  /* Change to your accent color */
}
```

### Add Your GitHub Link

Update the GitHub button in `index.html`:

```html
<a href="https://github.com/username/your-repo" class="btn btn-large btn-outline">
    <span>View on GitHub</span>
</a>
```

## 🔧 Connecting Backend to GitHub Pages

**Important**: GitHub Pages only hosts static files (HTML, CSS, JS). To connect the backend:

### Option 1: Deploy Backend Separately

1. **Deploy backend to a cloud service**:
   - Heroku (free tier available)
   - Railway.app
   - Render.com
   - DigitalOcean
   - AWS/Google Cloud

2. **Update dashboard.html** with your backend URL:

```javascript
// In dashboard.html, find this line:
const BACKEND_URL = 'http://localhost:5000';

// Change to your deployed backend URL:
const BACKEND_URL = 'https://your-backend-url.herokuapp.com';
```

### Option 2: Use Demo Mode

The dashboard already has a fallback to show demo data if the backend isn't connected. This works great for showcasing the project!

## 📱 Testing Your Deployment

1. Visit `https://username.github.io/`
2. Check that:
   - ✅ Navigation works
   - ✅ Buttons are clickable
   - ✅ Smooth scrolling works
   - ✅ Dashboard page loads
   - ✅ Responsive design works on mobile

## 🐛 Troubleshooting

### Issue: 404 Page Not Found

**Solution**: 
- Wait 5-10 minutes for GitHub to build your site
- Check that your repository is named correctly: `username.github.io`
- Ensure `index.html` exists in the root directory

### Issue: CSS/JS Not Loading

**Solution**:
- Check file paths in HTML:
  ```html
  <link rel="stylesheet" href="style.css">  <!-- NOT /style.css -->
  <script src="script.js"></script>         <!-- NOT /script.js -->
  ```
- File names are case-sensitive on GitHub Pages

### Issue: Dashboard Shows "Backend Not Connected"

**Solution**:
- This is expected if you haven't deployed the backend
- The dashboard will show demo data automatically
- To connect real backend, deploy it separately (see above)

## 🔄 Updating Your Site

Whenever you make changes:

**Using Web Interface**:
1. Navigate to the file on GitHub
2. Click the pencil icon (Edit)
3. Make changes
4. Click "Commit changes"
5. Wait 1-2 minutes for deployment

**Using Git**:
```bash
# Make your changes to files locally

# Add changes
git add .

# Commit
git commit -m "Updated dashboard design"

# Push to GitHub
git push origin main

# Wait 1-2 minutes for deployment
```

## 📊 Custom Domain (Optional)

To use your own domain (e.g., `smartagri.com`):

1. Buy a domain from a registrar (Namecheap, GoDaddy, etc.)
2. In GitHub repository settings → Pages
3. Enter your custom domain
4. Configure DNS at your domain registrar:
   ```
   Type: A
   Host: @
   Value: 185.199.108.153
   
   Type: A
   Host: @
   Value: 185.199.109.153
   
   Type: A
   Host: @
   Value: 185.199.110.153
   
   Type: A
   Host: @
   Value: 185.199.111.153
   
   Type: CNAME
   Host: www
   Value: username.github.io
   ```

## 📈 Analytics (Optional)

Add Google Analytics to track visitors:

1. Get your tracking code from [Google Analytics](https://analytics.google.com)
2. Add before `</head>` in `index.html` and `dashboard.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

## 🎉 You're Done!

Your Smart Agriculture AI website is now live on the internet!

Share it with:
- `https://username.github.io/` (Home page)
- `https://username.github.io/dashboard.html` (Dashboard)

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Custom Domains Guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Markdown Guide](https://guides.github.com/features/mastering-markdown/)

---

Need help? Check the [main README](README.md) or open an issue on GitHub!
