# Module 6 — GitLab CI/CD: Complete the Pipeline

**Goal:** Add the deploy stage so the pipeline does everything Module 5 still required by hand. This is "full CI/CD, push-based" — the most automated point of the day so far.

## Steps for students

1. Extend `.gitlab-ci.yml` with a `deploy` stage that runs `helm upgrade` from the runner itself:
   ```yaml
   stages:
     - build
     - push
     - deploy

   # ...(build and push stages unchanged from Module 5)...

   deploy:
     stage: deploy
     image: alpine/helm:3.14.0
     script:
       - helm upgrade --install devops-journey-app ./helm/devops-journey-app
           --set image.repository=$CI_REGISTRY_IMAGE
           --set image.tag=$CI_COMMIT_SHORT_SHA
           --set deployedBy=gitlab-cicd
           --kubeconfig $KUBE_CONFIG
     only:
       - main
   ```
   > Note: this assumes the chart lives in the same repo as the pipeline for simplicity today. Mention to students that in many real setups, `app-repo` and `manifests-repo` are separate, and this stage would need to fetch or trigger the manifests-repo instead — that separation is exactly why ArgoCD prefers watching a dedicated repo (foreshadow Module 7).
2. Add the `KUBE_CONFIG` CI/CD variable (File type) containing their kubeconfig, so the runner can reach the cluster.
3. Push a small change (bump a version string, change `APP_COLOR` default) and watch the full pipeline run: **build → push → deploy**, completely hands-off.
4. Refresh the browser — new version live, page now says `gitlab-cicd`, and nobody ran a manual command.

## Talking points — set up the Module 7 discussion
Don't resolve anything yet, just ask and write answers on the board:
- "Who has cluster credentials now?" → the GitLab runner, via `KUBE_CONFIG`.
- "If I edit something directly in the cluster right now with `kubectl`, does this pipeline know?" → No — it only runs on `git push`.
- "Is there anything continuously checking the cluster still matches what's in Git?" → No.

This is the most automated the day gets *without* GitOps — and it still has real gaps. Move straight into Module 7 while this is fresh.

## Common issues
- `KUBE_CONFIG` file variable formatting/masking issues in GitLab.