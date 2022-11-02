.PHONY: help
help:	## shows this help message
	@echo "Usage:\n\tmake <target>"
	@echo "\nAvailable targets:"
	@awk 'BEGIN {FS = ":.*##"; } /^[$$()% a-zA-Z_-]+:.*?##/ \
	{ printf "\t\033[36m%-30s\033[0m %s\n", $$1, $$2 } /^##@/ \
	{ printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##############################################################################
#################### CONTINOUS INTEGRATION RECIPES ###########################
##############################################################################

.PHONY: lock upgrade
lock:	## lock requirements
	@echo "locking base requirements..."
	pip-compile -v setup.cfg

	@echo "locking dev requirements..."
	pip-compile -v requirements-dev.in -o requirements-dev.txt \
	--strip-extras

upgrade:	## upgrade requirements
	@echo "upgrading base requirements..."
	pip-compile -v --upgrade setup.cfg

	@echo "upgrading dev requirements..."
	pip-compile -v --upgrade requirements-dev.in -o requirements-dev.txt \
	--strip-extras
