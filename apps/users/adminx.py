# users/adminx.py
import xadmin
from xadmin import views


class BaseSetting(object):
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 全局配置，后台管理标题和页脚
    site_title = "校园服务系统"
    # site_footer = "http://www.cnblogs.com/derek1184405959/"
    # 菜单收缩
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
