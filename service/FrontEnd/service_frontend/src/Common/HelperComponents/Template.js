import React from "react";

export function Template({ children }) {
  return (
    <div
      dangerouslySetInnerHTML={{
        __html: children
      }}
    />
  );
}

export function getCategoryServices({ category_name }) {}
