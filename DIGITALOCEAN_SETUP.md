# 🚀 DigitalOcean Deployment Guide for Wathaiq Plus

## 📋 Prerequisites
- DigitalOcean account
- GitHub repository connected to DigitalOcean
- Domain name (optional)

## 🔧 Step-by-Step Deployment

### 1. **Prepare Your Repository**
```bash
# Commit all changes
git add .
git commit -m "Add DigitalOcean deployment configuration"
git push origin main
```

### 2. **Create DigitalOcean App**
1. Go to [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)
2. Click "Create App"
3. Connect your GitHub repository
4. Select your repository and branch
5. Configure the app settings

### 3. **App Configuration**
Use the provided `digitalocean_app.yaml` or configure manually:

**Build Settings:**
- Build Command: `pip install -r requirements.txt`
- Run Command: `gunicorn project.wsgi:application --bind 0.0.0.0:8080`
- Source Directory: `/`

**Environment Variables:**
```
DJANGO_SETTINGS_MODULE=project.settings
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-postgresql-url
EMAIL_HOST_USER=your-email@domain.com
EMAIL_HOST_PASSWORD=your-email-password
```

### 4. **Database Setup**
1. Add a PostgreSQL database to your app
2. DigitalOcean will provide a `DATABASE_URL` environment variable
3. The app will automatically use this for database connections

### 5. **Deploy and Setup Test Accounts**

After deployment, run these commands in DigitalOcean's console:

```bash
# Run migrations
python manage.py migrate

# Create admin account
python manage.py createsuperuser --username admin --email admin@wathaiqplus.com

# Create test accounts
python manage.py create_test_accounts --count 10 --admin

# Collect static files
python manage.py collectstatic --noinput
```

## 🧪 Test Accounts Created

### Admin Account
- **URL**: `https://your-app.ondigitalocean.app/admin/`
- **Username**: `admin`
- **Password**: `admin123`

### Test Client Accounts
| Email | Password | Full Name |
|-------|----------|-----------|
| test1@wathaiqplus.com | test123456 | أحمد بن علي |
| test2@wathaiqplus.com | test123456 | فاطمة بنت محمد |
| test3@wathaiqplus.com | test123456 | محمد بن أحمد |
| test4@wathaiqplus.com | test123456 | عائشة بنت علي |
| test5@wathaiqplus.com | test123456 | علي بن عمر |

## 🔍 Testing Your Deployment

### 1. **Test User Registration**
- Visit your app URL
- Click "إنشاء حساب" (Create Account)
- Fill out the registration form
- Check email for verification code

### 2. **Test Admin Panel**
- Go to `/admin/`
- Login with admin credentials
- View and manage clients, services

### 3. **Test Service Requests**
- Login as a test client
- Go to "إضافة طلب جديد" (Add New Request)
- Submit a service request
- Check admin panel for the request

## 🛠️ Management Commands

### Create More Test Accounts
```bash
python manage.py create_test_accounts --count 5
```

### Create Admin Account
```bash
python manage.py create_test_accounts --admin
```

### Reset Database (Development Only)
```bash
python manage.py flush
python manage.py create_test_accounts --count 10 --admin
```

## 📊 Monitoring and Logs

### View Application Logs
1. Go to your DigitalOcean app dashboard
2. Click on "Runtime Logs" tab
3. Monitor for errors and performance

### Database Monitoring
1. Go to "Databases" in DigitalOcean
2. Click on your database
3. Monitor connections and performance

## 🔒 Security Considerations

### Environment Variables
- Never commit sensitive data to Git
- Use DigitalOcean's environment variables
- Rotate SECRET_KEY regularly

### Database Security
- Use SSL connections
- Regular backups
- Monitor access logs

## 🚀 Performance Optimization

### Static Files
- DigitalOcean automatically serves static files
- Use CDN for better performance
- Optimize images before upload

### Database
- Use connection pooling
- Monitor query performance
- Add database indexes as needed

## 📞 Support and Troubleshooting

### Common Issues
1. **Database Connection**: Check DATABASE_URL format
2. **Static Files**: Ensure collectstatic runs
3. **Email**: Verify SMTP settings
4. **Admin Access**: Check superuser creation

### Debug Mode
For development, set `DEBUG=True` in environment variables

## 🎯 Next Steps

1. **Custom Domain**: Configure your domain in DigitalOcean
2. **SSL Certificate**: Automatic with DigitalOcean
3. **Monitoring**: Set up alerts and monitoring
4. **Backups**: Configure automatic database backups
5. **Scaling**: Adjust instance size as needed

---

**🎉 Congratulations! Your Wathaiq Plus app is now deployed on DigitalOcean!**
