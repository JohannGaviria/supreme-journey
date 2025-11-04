# Colors for output
GREEN=\033[0;32m
BLUE=\033[0;34m
YELLOW=\033[1;33m
RED=\033[0;31m
NC=\033[0m # No Color

.PHONY: help new list complete

# Filter options
FILTER ?= all  # Can be: all, complete, incomplete
GREP_DATE = grep -l "✅.*Resuelta:.*[0-9]\\{4\\}-[0-9]\\{2\\}-[0-9]\\{2\\}"

list: ## List all katas (FILTER=all|complete|incomplete)
	@echo "$(YELLOW)=== Katas ===$(NC)"
	@for kata in $$(find daily-katas -name "problem.md"); do \
		dir=$$(dirname $$kata); \
		name=$$(basename $$dir | cut -d'-' -f4-); \
		if [ "$(FILTER)" = "complete" ] && ! echo "$$kata" | xargs $(GREP_DATE) > /dev/null; then \
			continue; \
		elif [ "$(FILTER)" = "incomplete" ] && echo "$$kata" | xargs $(GREP_DATE) > /dev/null; then \
			continue; \
		fi; \
		if echo "$$kata" | xargs $(GREP_DATE) > /dev/null; then \
			echo "$(GREEN)✓ $$name$(NC) ($$dir)"; \
		else \
			echo "$(RED)✗ $$name$(NC) ($$dir)"; \
		fi \
	done

complete: ## Mark a kata as completed (asks for kata name)
	@echo "$(YELLOW)Please enter the kata name:$(NC)"
	@read -p "Kata name: " KATA_NAME; \
	if [ -z "$$KATA_NAME" ]; then \
		echo "$(YELLOW)Error: Kata name cannot be empty$(NC)"; \
		exit 1; \
	fi; \
	KATA_PATH=$$(find daily-katas -type d -name "*$$KATA_NAME"); \
	if [ -z "$$KATA_PATH" ]; then \
		echo "$(RED)Error: Kata not found$(NC)"; \
		exit 1; \
	fi; \
	TODAY=$$(date +"%Y-%m-%d"); \
	sed -i "s/✅.*Resuelta:.*YYYY-MM-DD/✅ **Resuelta:** $$TODAY/" "$$KATA_PATH/problem.md"; \
	echo "$(GREEN)✓ Kata marked as completed: $$KATA_PATH$(NC)"

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
