from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from dependency import get_templates
from config.config import CONFIGS
import os

router = APIRouter()


def get_server_ips():
    env_file = '/etc/hysteria/.configs.env'
    ipv4, ipv6 = "", ""
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                if line.startswith('IP4='):
                    ipv4 = line.strip().split('=', 1)[1]
                elif line.startswith('IP6='):
                    ipv6 = line.strip().split('=', 1)[1]
    return ipv4, ipv6


@router.get('/')
async def settings(request: Request, templates: Jinja2Templates = Depends(get_templates)):
    ipv4, ipv6 = get_server_ips()
    return templates.TemplateResponse('settings.html', {'request': request, 'api_token': CONFIGS.API_TOKEN, 'ipv4': ipv4, 'ipv6': ipv6})


@router.get('/config')
async def config(request: Request, templates: Jinja2Templates = Depends(get_templates)):
    return templates.TemplateResponse('config.html', {'request': request})


@router.get('/nodes')
async def nodes(request: Request, templates: Jinja2Templates = Depends(get_templates)):
    panel_url = str(request.base_url).rstrip('/')
    return templates.TemplateResponse('nodes.html', {'request': request, 'api_token': CONFIGS.API_TOKEN, 'panel_url': panel_url})


@router.get('/hysteria')
async def hysteria_settings(request: Request, templates: Jinja2Templates = Depends(get_templates)):
    return templates.TemplateResponse('hysteria_settings.html', {'request': request})