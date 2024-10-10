# Color definitions
LIGHT_BLUE = \033[1;36m
RESET = \033[0m

.PHONY: test

test:
	@echo "$(LIGHT_BLUE)Running tests...$(RESET)"
	@docker exec python pytest --clear-cache
	@echo "$(LIGHT_BLUE)Tests completed.$(RESET)"