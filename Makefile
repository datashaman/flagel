serve-development: serve-backend serve-frontend compass-watch tail-logs

serve-backend:
	python apps/flagel/run.py >> logs/backend.log 2>&1 &

tail-logs:
	tail -f logs/*.log

serve-frontend:
	cd apps/flagel/static; python -m SimpleHTTPServer >> ../../../logs/frontend.log 2>&1 &

serve-production: build-static
	APP_ENV=production python apps/flagel/run.py

build-static:
	bin/r.js -o etc/flagel.build.js

compass-watch:
	cd apps/flagel; compass watch --quiet --boring >> ../../logs/compass.log 2>&1 &
