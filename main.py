#!/usr/bin/env python3

import os, subprocess, time
import docker
import colorama
from colorama import Fore
import configparser
import time

parser = configparser.ConfigParser()
parser.read("configfile.ini")
client = docker.from_env()
container = client.containers.get(f'{parser.get("general", "container_name")}')

# database_name = parser.get('general', 'database_name')
# test_database_name = parser.get('general', 'test_database_name')
databases = parser['databases_names']

def validate_container():
    # check if container exists
    if not container:
        print(Fore.RED + 'Container does not exist')
        exit()

def validate_container_status():
    # if container.status == 'exited' then print an error message and exit
    if container.status == 'exited':
        print(Fore.RED + 'Container is not running')
        exit()

def validate_backup_file():
    # check if backup file exists
    if not os.path.isfile(parser.get('general', 'docker_storage_dir') + '/backup.sql'):
        print(Fore.RED + 'No se encontró el archivo de backup, asegurese de haberlo generado')
        exit()

def restore_database(database_name):
    # create .cnf file for mysql with the user and password to connect to the database, check: https://stackoverflow.com/questions/62287061/connect-to-2-instances-of-mysql-with-no-password-interaction-using-command-line
    mysql_command = f"drop database if exists {database_name}; create database {database_name}; use {database_name}; source backup.sql;"
    result = container.exec_run(f'mysql -e"{mysql_command}"', workdir='/home/database_backup/', user='root', stdin=False)

def main():
    st = time.time()

    print(Fore.WHITE + f'Short id: {container.short_id}')
    print(Fore.GREEN + f'Estado: {container.status}')
    print(Fore.GREEN + f'Image: {container.image}')

    validate_container()
    validate_container_status()
    validate_backup_file()

    print(Fore.WHITE + 'Backup encontrado')

    print('Databases:')
    for key in databases:
        print(f'Restaurando Base de datos: {databases[key]}')
        restore_database(databases[key])

    et = time.time()
    elapsed_time = et - st
    # Aprox 1000 segundos, 16 minutos en pruebas para db de talently
    print(Fore.YELLOW + 'Execution time:', elapsed_time, 'seconds')
    print(Fore.GREEN + 'Restauración completada')

main()
