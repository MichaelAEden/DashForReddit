import React from 'react';

export default function Subreddit(props) {
  const { subreddit } = props;

  return (
    <div className="Subreddit">
      <h1>{subreddit.displayName}</h1>
      <p>Subscribers: {subreddit.subscriptionCount}</p>
    </div>
  );
}
