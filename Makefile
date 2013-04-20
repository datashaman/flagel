serve-development:
	@python apps/flagel/run.py

serve-production: build-static
	@APP_ENV=production python apps/flagel/run.py

build-static:
	@bin/r.js -o etc/flagel.build.js
