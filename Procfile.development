backend: python apps/flagel/run.py 2>&1 | tee -a logs/backend.log
frontend: bash -c "cd apps/flagel/static; python -m SimpleHTTPServer 2>&1 | tee -a ../../../logs/frontend.log"
compass: bash -c "cd apps/flagel; bundle exec compass watch --quiet"
