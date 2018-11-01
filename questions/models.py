from django.db import models

# 用户
class UserInfo(models.Model):
    def __str__(self):
        return self.u_login_name
    u_create_datetime = models.DateTimeField(auto_now_add = True)
    u_real_name = models.CharField(max_length = 20,null = True,blank = True)
    u_login_name = models.CharField(max_length = 20)
    u_pwd = models.CharField(max_length = 20)
    u_last_login_datetime = models.DateTimeField(auto_now=True,null = True)
    u_last_login_ip = models.CharField(max_length = 20,null = True)

# 问题来源
class QuestionSource(models.Model):
    def __str__(self):
        return self.q_source
    q_source = models.CharField(max_length = 100)

# 问题解决情况
class QuestionSolve(models.Model):
    def __str__(self):
        return self.s_solve
    s_solve = models.CharField(max_length = 20)

# 科目信息
class SubjectInfo(models.Model):
    def __str__(self):
        return self.s_name
    s_name = models.CharField(max_length = 20)

# 问题记录管理器
class QstCommentManager(models.Manager):
    def all(self):
        return super().all().filter(isDelete=False)
    def create(self,title,source,hpTime):
        qst_cmt = QuestionComment()
        qst_cmt.c_title = title
        qst_cmt.c_qst_source = source
        qst_cmt.c_happen_date = hpTime
        qst_cmt.c_solve = QuestionSolve.objects.get(id=1)
        return  qst_cmt.save()

# 问题记录
class   QuestionComment(models.Model):
    def __str__(self):
        return self.c_comment
    c_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE) # 操作人
    c_subject = models.ForeignKey('SubjectInfo', on_delete=models.CASCADE,null =True) #科目
    c_title = models.CharField(max_length = 100,null = True, blank = True) # 问题标题
    c_qst_source = models.ForeignKey('QuestionSource', on_delete=models.CASCADE)  # 问题来源
    c_solve = models.ForeignKey('QuestionSolve',on_delete=models.CASCADE,) # 问题解决：未开始处理、未完成、不满意解决、满意解决
    c_happen_date = models.DateTimeField(auto_now_add = True) # 发生时间，auto_now包括更新的时间  和 auto_now_add仅创建时的时间，更新时不改动
    c_resolvent = models.TextField(null = True) # 解决方法
    c_resolvent_date = models.DateTimeField(null = True) # 解决时间
    isDelete = models.BooleanField(default = False)
    # 添加类管理器
    objects = QstCommentManager()
