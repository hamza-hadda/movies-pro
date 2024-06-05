# Movies Pro

## Running the Application

To run the application using Docker, you can use the following commands:

```bash
docker-compose build
docker-compose up
```
If you encounter any issues running the Vue.js application with Docker, you can manually run it using npm:

```bash
cd movies_web/
npm install
npm run serve
```

once the application is up you can comment the method `ready` inside `movie_core/core/apps`