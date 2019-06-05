import React from "react";

export function Template({ children }) {
  console.log(children);
  return <template dangerouslySetInnerHTML={{ __html: children }} />;
}

export function getCategoryServices({ category_name }) {}
