# Module 2 — Manual Kubernetes Deploy (11:00 – 11:45)

## Steps for students

1. Edit `manifests/deployment.yaml`:
   - set `image:` to the image they pushed in Module 1
   - set `DEPLOYED_BY` to `"manual-kubectl"`
2. Apply both manifests:
   ```bash
   kubectl apply -f manifests/deployment.yaml
   kubectl apply -f manifests/service.yaml
   ```
3. Check it's running:
   ```bash
   kubectl get pods
   kubectl get svc
   ```
4. Open the app via NodePort (or `kubectl port-forward svc/flask-app 8080:80`) and confirm the page shows `manual-kubectl`.

## Live "break it" demo (do this yourself in front of them)

```bash
kubectl set image deployment/flask-app app=tokashawky/flask-app2:v1
```
Ask: *"If I did this from my own laptop right now, would any of you know? Would Git show this change anywhere?"*

## Discussion questions to ask out loud (don't answer yet — just plant them)

- Who has `kubectl` access to this cluster in a real team?
- If two people apply manifests independently, how do you know what's actually live?
- If someone edits something directly in the cluster, does anything tell you it no longer matches your YAML files?

