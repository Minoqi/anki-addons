

from aqt import mw

# https://atomiks.github.io/tippyjs/

TIPPY_FOLDER = "tippy"

mw.addonManager.setWebExports(
    __name__,
    rf"(custom_by_shige/{TIPPY_FOLDER})/.*(js|css)"
)



def get_tooltip():

    addon_package = mw.addonManager.addonFromModule(__name__)
    tippy_folder_path = f"/_addons/{addon_package}/custom_by_shige/{TIPPY_FOLDER}"

    shige_custom_tooltip  = f"""
    <link rel="stylesheet" href="{tippy_folder_path}/tippy.css">
    <link rel="stylesheet" href="{tippy_folder_path}/scale.css">
    <script src="{tippy_folder_path}/popper.min.js"></script>
    <script src="{tippy_folder_path}/tippy.umd.min.js"></script>

    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        document.querySelectorAll('.custom_shige_tooltip').forEach(function(element) {{
            tippy(element, {{
                content: element.querySelector('.custom_shige_tooltiptext').innerHTML,
                allowHTML: true,
                animation: 'scale',
                theme: 'custom',
                onShow(instance) {{
                    const tippyBox = instance.popper.querySelector('.tippy-box');
                    tippyBox.style.backgroundColor = '#009bb6';
                    const tippyArrow = instance.popper.querySelector('.tippy-arrow');
                    tippyArrow.style.color = '#009bb6';
                }}
            }});
        }});
    }});
    </script>
    """

    return shige_custom_tooltip




    # <script>
    # document.addEventListener('DOMContentLoaded', function() {{
    #     document.querySelectorAll('.custom_shige_tooltip').forEach(function(element) {{
    #         tippy(element, {{
    #             content: element.querySelector('.custom_shige_tooltiptext').innerHTML,
    #             allowHTML: true,
    #             animation: 'scale',
    #             theme: 'custom',
    #             onShow(instance) {{
    #                 const tippyBox = instance.popper.querySelector('.tippy-box');
    #                 tippyBox.style.backgroundColor = 'rgba(0, 0, 255, 0.5)';
    #                 const tippyArrow = instance.popper.querySelector('.tippy-arrow');
    #                 tippyArrow.style.color = 'rgba(0, 0, 255, 0.5)';
    #             }}
    #         }});
    #     }});
    # }});
    # </script>


    # <script>
    # document.addEventListener('DOMContentLoaded', function() {{
    #     document.querySelectorAll('.custom_shige_tooltip').forEach(function(element) {{
    #         tippy(element, {{
    #             content: element.querySelector('.custom_shige_tooltiptext').innerHTML,
    #             allowHTML: true,
    #             animation: 'scale',
    #             theme: 'custom',

    #         }});
    #     }});
    # }});
    # </script>