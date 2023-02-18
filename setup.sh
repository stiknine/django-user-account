#!/bin/sh
#
# Setup a Django project which implements a customer user model,
# environment variable configuration (.env), Django and auth logging
# and a basic project layout.

SCRIPT_PATH=$(cd $(dirname $0) ; pwd -P)

print_usage() {
  printf "\n"
  printf "Project template for Django set up.\n"
  printf "Usage: setup.sh [-n <name>] [-p <path>]\n"
  printf "       -n <name>\n"
  printf "              Project name.\n"
  printf "              Recommended to be a single lowercase word or underscore for separator.\n\n"
  printf "       -p <path>\n"
  printf "              Full path to your project. Directory must exist.\n\n"
  printf "       -h\n"
  printf "              Prints out this help page.\n\n"
}

while getopts ":n:p:h" OPTION; do
  case "${OPTION}" in
    n)
      PROJECT_NAME="$OPTARG"
      ;;
    p)
      PROJECT_PATH="${OPTARG%/}"
      ;;
    h|\?)
      print_usage
      exit 0
      ;;
    :)
      echo "Option -$OPTARG requires an argument."
      print_usage
      exit 1
      ;;
  esac
done

if [ "$PROJECT_NAME" = "" ] || [ "$PROJECT_NAME" = "-p" ]; then
  echo "No project name provided."
  print_usage
  exit 1
fi

if [ ! -d "$PROJECT_PATH" ]; then
  echo "Project path does not exist."
  print_usage
  exit 1
fi

# Install and set up project
echo "*** Set up project..."
cd "$PROJECT_PATH"
cp "${SCRIPT_PATH}/requirements.txt" "$PROJECT_PATH"
cp "${SCRIPT_PATH}/.gitignore" "$PROJECT_PATH"

echo "*** Create Python virtual environment.\n"
python3 -m venv venv
source venv/bin/activate
pip3 install -U pip
pip3 install -r requirements.txt
deactivate
source venv/bin/activate

echo "\n*** Create Django project ($PROJECT_NAME)."
django-admin startproject "$PROJECT_NAME"
deactivate

echo "*** Copy project files."
cd "$PROJECT_NAME"
cp -R "${SCRIPT_PATH}/account/user" .
cp -R "${SCRIPT_PATH}/account/templates" .
cp -R "${SCRIPT_PATH}/account/static" .
cp -R "${SCRIPT_PATH}/account/account/.env.dist" "${PROJECT_NAME}/"
cp -R "${SCRIPT_PATH}/account/account/.env.dist" "${PROJECT_NAME}/.env"
cp -R "${SCRIPT_PATH}/account/account/urls.py" "${PROJECT_NAME}/"
cp -R "${SCRIPT_PATH}/account/account/settings.py" "${PROJECT_NAME}/"
sed -i '' "s|'account.urls'|'${PROJECT_NAME}.urls'|" "${PROJECT_NAME}/settings.py"
sed -i '' "s|'account.wsgi.application'|'${PROJECT_NAME}.wsgi.application'|" "${PROJECT_NAME}/settings.py"

printf "Would you like to create a self-signed SSL cert? (yes/no) "
read MAKE_CERT
case "$MAKE_CERT" in
  y|Y|yes)
    openssl genrsa -out local.key 2048
    openssl req -new -key local.key -out local.csr
    openssl x509 -req -days 3650 -in local.csr -signkey local.key -out local.crt
    ;;
  *)
    ;;
esac

echo "*** Project set up complete.\n"
printf "*** Post set up tasks:\n"
printf "  Create database. If not using MySQL, install any necessary python packages\n"
printf "    and update the DATABASES option in the settings.py file.\n"
printf "  Modify the ${PROJECT_NAME}/.env file with your configuration options.\n"
printf "  Run the following commands within the project directory:\n"
printf "    (venv) $ python manage.py makemigrations\n"
printf "    (venv) $ python manage.py migrate\n"
printf "    (venv) $ python manage.py runserver_plus --cert-file local.crt --key-file local.key\n"
printf "\n\n"
