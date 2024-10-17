# Color definitions
LIGHT_BLUE = \033[1;36m
RESET = \033[0m

.PHONY: test

test:
	@echo "$(LIGHT_BLUE)Running tests...$(RESET)"
	@docker exec python python -m unittest discover -s tests -p "*Test.py"
	@echo "$(LIGHT_BLUE)Tests completed.$(RESET)"