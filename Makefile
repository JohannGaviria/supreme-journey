# Colors for output
GREEN=\033[0;32m
BLUE=\033[0;34m
YELLOW=\033[1;33m
RED=\033[0;31m
NC=\033[0m # No Color

.PHONY: help new

help: ## Show this help message
	@echo "$(YELLOW)=== Available Commands ===$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-16s$(NC) %s\n", $$1, $$2}'


new: ## Create new kata structure
	@echo "$(YELLOW)Please enter the kata name:$(NC)"
	@read -p "Kata name: " KATA_NAME; \
	if [ -z "$$KATA_NAME" ]; then \
		echo "$(YELLOW)Error: Kata name cannot be empty$(NC)"; \
		exit 1; \
	fi; \
	DATE=$$(date +"%Y-%m-%d"); \
	DIR_NAME="daily-katas/$$DATE-$$(echo "$$KATA_NAME" | tr ' ' '-' | tr '[:upper:]' '[:lower:]' | tr -cd '[:alnum:]-')"; \
	mkdir -p "$$DIR_NAME"; \
	cp templates/problem_template.md "$$DIR_NAME/problem.md"; \
	sed -i "s/{{KATA_TITLE}}/$$KATA_NAME/" "$$DIR_NAME/problem.md"; \
	sed -i "s/{{KATA_CREATED}}/$$DATE/" "$$DIR_NAME/problem.md"; \
	touch "$$DIR_NAME/solution.py"; \
	touch "$$DIR_NAME/test_solution.py"; \
	echo "$(GREEN)✓ Kata structure created: $$DIR_NAME$(NC)"
