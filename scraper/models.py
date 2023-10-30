from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime

class Base(DeclarativeBase):
    pass

class JiraIssue(Base):
    __tablename__ = 'jira_issues'
    id = Column(Integer, primary_key=True)
    key = Column(String)
    summary = Column(String)
    description = Column(String)
    status = Column(String)
    created = Column(DateTime)
    updated = Column(DateTime)
    resolved = Column(DateTime)
    reporter = Column(String)
    assignee = Column(String)
    priority = Column(String)
    labels = Column(String)
    
class GithubPullRequest(Base):
    __tablename__ = 'github_pull_requests'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    title = Column(String)
    body = Column(String)
    created = Column(DateTime)
    updated = Column(DateTime)
    author = Column(String)
    assignee = Column(String)
    labels = Column(String)
    reviewers = Column(String)
    reactions = Column(Integer)
    
class GithubComment(Base):
    __tablename__ = 'github_comments'
    id = Column(Integer, primary_key=True)
    issue_number = Column(Integer)
    body = Column(String)
    created = Column(DateTime)
    updated = Column(DateTime)
    author = Column(String)
    reactions = Column(Integer)