# 🚀 DevOps Flask App

![CI](https://github.com/MeirVEY770/devops-flask-app/actions/workflows/ci.yml/badge.svg)

## 📌 О проекте

Pet-проект, демонстрирующий полный DevOps pipeline:

**Code → CI/CD → Docker Hub → Kubernetes → Browser**

Приложение автоматически собирается, публикуется и разворачивается в Kubernetes.

---

## 🧰 Технологии

- Python (Flask)
- Docker
- GitHub Actions (CI/CD)
- Docker Hub
- Kubernetes (Minikube)

---

## ⚙️ CI/CD Pipeline

При каждом `git push`:

- 🔄 собирается Docker image  
- 🔐 используется авторизация через GitHub Secrets  
- 📦 образ отправляется в Docker Hub  
- 🚀 готов к деплою в Kubernetes  

Docker Hub:

👉 https://hub.docker.com/r/elik770/devops-flask-app

---

## 🐳 Docker (локальный запуск)

```bash
cd app
docker build -t devops-flask-app .
docker run -p 3000:3000 devops-flask-app
