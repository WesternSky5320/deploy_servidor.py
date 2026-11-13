import os

# 1. Atualizacao do sistema
os.system("dnf upgrade -y --refresh")

# 2. Instalacao do Apache (httpd) e do Git
os.system("dnf install -y httpd git")

# 3. Gerenciamento do servico
os.system("systemctl start httpd")
os.system("systemctl enable httpd")

# 4. Deploy da aplicacao
os.system("git clone https://github.com/denilsonbonatti/mundo-invertido.git /tmp/mundo-invertido")
os.system("cp -r /tmp/mundo-invertido/* /var/www/html/")
os.system("rm -rf /tmp/mundo-invertido")

# 5. Permissoes e contexto SELinux
os.system("chown -R apache:apache /var/www/html/")
os.system("restorecon -R /var/www/html/")

print("Servidor web publicado com sucesso.")
