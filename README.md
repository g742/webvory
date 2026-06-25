                ┌──────────────┐
                │   GitHub     │
                └──────┬───────┘
                       │ CI/CD
                       ▼
              ┌─────────────────┐
              │Ubuntu Local Server│
              └──────┬──────────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   ┌────────┐  ┌────────┐  ┌──────────┐
   │ NGINX  │  │ FastAPI│  │  Redis   │
   └────┬───┘  └────┬───┘  └────┬─────┘
        │           │            │
        ▼           ▼            ▼
                 ┌────────────┐
                 │ PostgreSQL │
                 └────────────┘


======================================= Find the given video and related documents ==========================================

Deploy FastAPI app on local ubuntu server ( Can scale up and down if on cloud to prevent downtime with different AZs ).

Deploy on Docker container through Docker-compose.

for security to prevent from DDOS attack I setup fail2ban on server and allow only port related to application.

for backup use cronjob for DB backup.

Backend API kept in github secrets.

Health check use http://localhost/metrics

For Monitoring use prometheus to collect metrics and visualization use grafana and check number of hit or click on app and other infrastructure. 
