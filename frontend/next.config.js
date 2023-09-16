module.exports = () => {
  const rewrites = () => {
    return [
      {
        source: "/hello/:path*",
        destination: "http://localhost:5000/api/hello/:path*",
      },
    ];
  };
  return {
    rewrites,
  };
};
