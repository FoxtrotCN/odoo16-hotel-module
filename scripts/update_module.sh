#!/bin/bash
docker compose -f ~/Desktop/odoo-projects/odoo-hotel/docker-compose.yml run --rm odoo odoo -u hotel -d hotel_dev --stop-after-init