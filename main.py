#!/usr/bin/env python3

import os, subprocess, time
import docker
import colorama
from colorama import Fore
# from configparser import ConfigParser
import configparser
import time

projectDir = '/Users/diego/sites/talently/l9-ops-backend-api'
dockerStorageDir = '/Users/diego/sites/talently/l9-ops-backend-api/docker/storage/databases_backup'


def main():
    st = time.time()
    # docker exec -it leacy php artisan tinker
    client = docker.from_env()
    # container = client.containers.get('leacy')
    container = client.containers.get('mysql')

    # container.logs()
    print(Fore.WHITE + f'Short id: {container.short_id}')
    print(Fore.GREEN + f'Estado: {container.status}')
    print(Fore.GREEN + f'Image: {container.image}')

    # if container.status == 'exited' then print an error message and exit
    if container.status == 'exited':
        print(Fore.RED + 'Container is not running')
        exit()



    print(Fore.WHITE + 'Verificando existencia de backup...')
    if not os.path.isfile(dockerStorageDir + '/backup.sql'):
        print(Fore.RED + 'No se encontró el archivo de backup, asegurese de haberlo generado')
        exit()


    print(Fore.WHITE + 'Backup encontrado, restaurando...')

    # create .cnf file for mysql with the user and password to connect to the database, check: https://stackoverflow.com/questions/62287061/connect-to-2-instances-of-mysql-with-no-password-interaction-using-command-line

    mysql_command = "drop database if exists leacy; create database leacy; use leacy; source backup.sql;"
    result = container.exec_run(f'mysql -e"{mysql_command}"', workdir='/home/database_backup/', user='root', stdin=False)

    et = time.time()
    elapsed_time = et - st
    # Aprox 1000 segundos, 16 minutos en pruebas
    print(Fore.YELLOW + 'Execution time:', elapsed_time, 'seconds')
    print(Fore.GREEN + 'Restauración completada')

main()
