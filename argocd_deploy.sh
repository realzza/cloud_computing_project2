argocd app create zz188-american-predictor \
 --repo https://github.com/realzza/cloud_computing_project2 \
 --path . \
 --project zz188-project \
 --dest-namespace zz188 \
 --dest-server https://kubernetes.default.svc \
 --sync-policy auto