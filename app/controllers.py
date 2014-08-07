# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from app import app, db

from app.forms import ArticleForm, CommentForm
from app.models import Article, Comment


@app.route('/', methods=['GET'])
def article_list():
    context = {}
    context['article_list'] = Article.query.order_by(
        desc(Article.date_created)).all()

    return render_template('home.html', context=context, active_tab='article_list')


@app.route('/article/create/', methods=['GET', 'POST'])
def article_create():
    form = ArticleForm()
    if request.method == 'GET':
        return render_template('article/create.html', form=form, active_tab='article_create')
    elif request.method == 'POST':
        if form.validate_on_submit():
            # 사용자가 입력한 글 데이터로 Article 모델 인스턴스를 생성한다.
            article = Article(
                title=form.title.data,
                author=form.author.data,
                category=form.category.data,
                content=form.content.data
            )
            # 데이터베이스에 데이터를 저장할 준비를 한다. (게시글)
            db.session.add(article)
            # 데이터베이스에 저장하라는 명령을 한다.
            db.session.commit()

            flash(u'게시글을 작성하였습니다.', 'success')
            return redirect(url_for('article_list'))
        return render_template('article/create.html', form=form, active_tab='article_create')
