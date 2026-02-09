## [Update] - 2026-02-09 - v1.4.6

### Added
- **Port Hopping**: Новая функция Port Hopping в настройках Hysteria. Позволяет перенаправлять диапазон UDP-портов на серверный порт через iptables/ip6tables NAT PREROUTING. Клиенты переключаются между портами для обхода throttling провайдера.
- **Port Hopping API**: Три новых эндпоинта — `GET /port-hopping/status`, `POST /port-hopping/enable`, `POST /port-hopping/disable`.
- **Port Hopping UI**: Карточка управления Port Hopping на странице Hysteria Settings (включение/выключение, задание диапазона портов, отображение статуса и активных iptables-правил).
- **Port Hopping в URI**: При активном Port Hopping пользовательские URI автоматически содержат диапазон портов вместо одиночного порта (формат `hy2://user:pass@ip:20000-50000?params`).
