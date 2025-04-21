# 🧠 AI Code Assistant

Python programlama için yapay zekâ destekli bir kod üretici asistan.  
Kullanıcıdan alınan doğal dil girdisine göre Python kodu ve başlık önerisi üretir.  
Flask, Docker ve Kubernetes (Minikube) teknolojileri kullanılarak geliştirildi.

## ✨ Özellikler

- Basit bir web arayüzü (Flask + HTML)
- Ollama ile yerel LLM entegrasyonu
- Prompt ile kod ve başlık üretimi
- Docker imajı olarak paketlenmiş
- Minikube üzerinde çalışır durumda

## 🛠 Teknolojiler

- Python 3.10
- Flask
- Ollama (LLM)
- Docker
- Kubernetes (Minikube)

## 📦 Kurulum

> Geliştirme ortamı: macOS (Apple Silicon)

1. Ollama kurulumu ve model yükleme:
```
brew install ollama
ollama pull codellama
ollama serve
```

2. Uygulama Docker imajını oluştur:
```
docker build -t codegen-assistant --no-cache .
```

3. Minikube imajını içeri al:
```
minikube image load codegen-assistant
```

4. Kubernetes bileşenlerini başlat:
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## 🌐 Uygulamayı Çalıştırma

Minikube dış IP'si bazı macOS sistemlerde doğrudan erişilebilir olmayabilir.  
Bu nedenle test için `port-forward` kullanabilirsiniz:

```
kubectl port-forward service/codegen-service 5000:5000
```

Tarayıcıda şu adrese gidin:

```
http://localhost:5000
```

> Eğer dış IP kullanmak istenirse `minikube tunnel` açılmalıdır.


## 📁 Proje Yapısı

```
.
├── app.py
├── main.py
├── ollama_client.py
├── Dockerfile
├── requirements.txt
├── templates/
│   ├── form.html
│   └── results.html
├── deployment.yaml
└── service.yaml
```

## 📌 Not

Bu uygulama test ve geliştirme amaçlıdır.  
Ollama modeli yerel olarak çalıştığı için kurulum yapılmadan çalışmaz.  
Model ismi (`codellama`) `ollama_client.py` içinde değiştirilerek özelleştirilebilir.

## 👤 Geliştirici

> Erdem Tahir Özyön  
> Ankara Üniversitesi - Yazılım Mühendisliği  
> ✉️ ozyonerdem@hotmail.com
