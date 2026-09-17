# Module 1 — Docker Recap (10:20 – 11:00)
## Steps for students


app >> dockerfile >> image >> container 






1. Clone/copy the `app/` folder.
2. Build the image:
   ```bash
   docker build -t <your-registry>/flask-app:v1 ./app
   ```
3. Run it locally and check the browser:
   ```bash
   docker run -p 5000:5000 <your-registry>/flask-app:v1
   ```
   Open `http://localhost:5000` — they should see a dark-blue page saying "Version: v1".
4. Change `APP_COLOR` or `APP_VERSION` at runtime to prove the app reads env vars:
   ```bash
   docker run -p 5000:5000 -e APP_COLOR="#e74c3c" -e APP_VERSION="v2" <your-registry>/flask-app:v1
   ```
   ```ini
                           Docker Host
                     ┌─────────────────┐
                     │                 │
         Browser     │    Container    │
         localhost   │                 │
         :5000       │  /app           │
         ───────►    │  app.py         │
                     │     │           │
                     │     ▼           │
                     │ Python :5000    │
                     └─────────────────┘

   ```
   Refresh the browser — page is now red and says v2. **Remember this page — you'll watch it change all day.**
5. Log in and push:
   ```bash
   docker login <your-registry>
   docker push <your-registry>/devops-journey-app:v1
   ```

## Talking points while they work
- Now that the image is in the registry — how does it get into a running cluster?.
