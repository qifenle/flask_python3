from . import passport_blue
# 导入flask内置对象
from flask import request,jsonify,current_app,make_response
# 导入自定义状态码
from info.utils.response_code import RET
# 导入图片验证码工具
from info.utils.captcha.captcha import captcha
# 导入redis数据库，用来存储图片验证码
from info import redis_store,constants


@passport_blue.route('/image_code')
def generate_image_code():
    # 获取参数
    image_code_id = request.args.get('image_code_id')
    # 检查参数，如果没有uuid，直接返回自定义状态码
    if not image_code_id:
        return jsonify(errno=RET.PARAMERR,errmsg='参数错误')
    # 调用扩展，生成图片验证码
    name,text,image = captcha.generate_captcha()
    try:
        redis_store.setex('ImageCode_' + image_code_id,constants.IMAGE_CODE_REDIS_EXPIRES,text)
    except Exception as e:
        # 记录错误信息到日志文件中
        current_app.logger.error(e)
        # 如过保存数据不成功,返回错误信息
        return jsonify(error=RET.DBERR,errmsg='保存数据失败')
    else:
        # 如果保存成功，返回图片，使用响应对象，直接返回图片
        response = make_response(image)
        # 修改响应报文的类型
        response.headers['Content-Type'] = 'image/jpg'
        # 返回响应，响应报文的默认类型Content-Type=‘text/html’
        return response
    pass