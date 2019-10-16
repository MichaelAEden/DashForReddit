import React from 'react';

import Subreddit from '../Subreddit';

export default function SubredditNav(props) {
  const subreddits = [
    { displayName: 'uwaterloo', subscriptionCount: 44444 },
    { displayName: 'UofT', subscriptionCount: 3 }
  ];

  return (
    <div className="SubredditNav">
      {subreddits.map((subreddit, i) => (
        <Subreddit key={i} subreddit={subreddit} />
      ))}
    </div>
  );
}
