# Usa una imagen base de Node.js
FROM node:14

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el package.json y el package-lock.json a la imagen
COPY package*.json ./

# Instala las dependencias de la aplicación
RUN npm install

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["npm", "start"]