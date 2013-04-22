install:
	pip install -r etc/requirements.pip
	bower install
	bundle install

serve-development: compass-development-compile
	bundle exec foreman start -f Procfile.development

serve-production: compass-production-compile build-static
	bundle exec foreman start -f Procfile.production

tail-logs:
	tail -f logs/*.log

build-static:
	bin/r.js -o etc/flagel.build.js

compass-development-compile:
	cd apps/flagel; bundle exec compass compile --force >> ../../logs/compass.log 2>&1 &

compass-production-compile:
	cd apps/flagel; bundle exec compass compile -e production --force >> ../../logs/compass.log 2>&1 &
