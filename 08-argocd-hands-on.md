# Module 8 — ArgoCD Hands-On (15:25 – 16:05)

## Pre-workshop install (do this BEFORE the day)

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl port-forward svc/argocd-server -n argocd 8080:443
```
Get the initial admin password ahead of time (or as the first live step):
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```
Install the `argocd` CLI on student machines beforehand: https://argo-cd.readthedocs.io/en/stable/cli_installation/

---

## Part A — Meet the UI (15:25 – 15:35)

1. Open `https://localhost:8080`, log in as `admin`.
2. Tour: empty Applications list, Settings → Repositories, Settings → Clusters.
3. Add `manifests-repo` as a known repo (UI: Settings → Repositories → Connect Repo, or CLI):
   ```bash
   argocd repo add https://gitlab.com/YOUR_GROUP/manifests-repo.git --username <user> --password <token>
   ```

## Part B — Deploy the same chart, the Argo way (15:35 – 15:50)

1. In `argocd/application.yaml`, point `repoURL` at their `manifests-repo` and `path` at `helm/devops-journey-app`.
2. Apply the Application:
   ```bash
   kubectl apply -f argocd/application.yaml
   ```
3. Watch it appear in the UI: **Syncing → Synced / Healthy**, resource tree (Deployment → ReplicaSet → Pod → Service).
4. Open the app in the browser — same page, now `deployedBy: argocd`.

**Checkpoint:** every student's Application should show green "Synced" + "Healthy" before continuing.

## Part C — Self-heal demo (15:50 – 15:58) — the moment that sells GitOps

Have each student run this on their own cluster:
```bash
kubectl scale deployment devops-journey-app --replicas=5
```
or
```bash
kubectl set image deployment/devops-journey-app app=some-wrong-image
```
Watch the UI flip to **OutOfSync**, then auto-revert to match Git if `selfHeal: true`. This lands far better as something they trigger themselves than something they only watch you do.

## Part D — Full GitOps loop: change via Git only (15:58 – 16:05)

1. In `manifests-repo`, edit `helm/devops-journey-app/values.yaml` — change `appColor`/`appVersion`.
2. Commit, push. **No `kubectl` or `helm` command runs at all.**
3. Watch ArgoCD detect the change and auto-sync (or click "Sync" if `automated` isn't enabled).
4. Refresh the browser — new color/version, and nobody touched the cluster directly.

This closes the full loop: the same deploy they did manually (Module 3), then via Helm (Module 4), then via CI/CD (Module 6) — now driven entirely by a `git push` into `manifests-repo`.

## Common issues
- `selfHeal` can take a minute — mention ArgoCD's default polling interval vs. hitting "Refresh" in the UI to force an immediate check.
- Repo auth failures — use a GitLab access token with `read_repository` scope, pre-tested.
- If ArgoCD needs to render the Helm chart, confirm the Application's `source.helm` section (or that Argo auto-detects `Chart.yaml`) — test this once before the day.
