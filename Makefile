serve:
	cd frontend/recepies.generated.online/src ; npm run serve

deploy:
	cd frontend/recepies.generated.online/src ; npm run build  && firebase deploy