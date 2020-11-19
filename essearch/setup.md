ES Setup
- Install ES
    - wget -q0 - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add dfsd
    - sudo apt-get install apt-transport-https
    - echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
    - apt-get update && apt-get install elasticsearch


