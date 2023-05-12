from board.models import Token, Post


def update_tokens_is_upper_60_percent():
    """
    Token의 전체 게시글중 60%이상에서 발견여부를 업데이트
    """

    # 전체 Token
    tokens = Token.objects.all()
    # 전체 Post 갯수
    posts_count = Post.objects.count()

    for token in tokens:
        # Token을 포함하고 있는 Posts
        posts = Post.objects.filter(posttoken__token=token)

        # Token의 기존 상태
        current_ist_upper_60_percent = token.is_upper_60_percent

        # 새로운 Token의 상태
        # Token을 포함하고 있는 Posts가 전체의 60% 이상인지 확인
        new_is_upper_60_percent = posts.count() >= posts_count * 0.6

        if current_ist_upper_60_percent != new_is_upper_60_percent:
            # 상태가 변경된 경우 업데이트
            token.is_upper_60_percent = new_is_upper_60_percent
            token.save()
