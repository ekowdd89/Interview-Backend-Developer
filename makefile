.PHONY: backend frontend

backend:
	@echo "Building backend"
	@cd backend && poetry run uvicorn backend.main:app --reload --host 0.0.0.0 --port 8001

frontend:
	@make -C frontend