from django.contrib import admin
from .models import Share, Post, Comment, Like

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'image', 'date', 'get_likes', 'get_comments', 'get_shares']

    def get_likes(self, obj):
        return ", ".join([like.user.username for like in obj.likes.all()])
    get_likes.short_description = 'Likes'

    def get_comments(self, obj):
        return ", ".join([comment.comment for comment in obj.comments.all()])
    get_comments.short_description = 'Comments'

    def get_shares(self, obj):
        return ", ".join([share.user.username for share in obj.shares.all()])
    get_shares.short_description = 'Shares'

class ShareAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'share']

class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'like']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'comment']

admin.site.register(Share, ShareAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
