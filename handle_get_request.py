#!/usr/bin/env python3
"""Simple HTTP server in python for logging requests."""

import json
import logging
from argparse import ArgumentParser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


class RequestHandler(BaseHTTPRequestHandler):
    """Handle HTTP request."""

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info(f"GET request,\nPath: {self.path}\n")
        self._set_response()
        query_str = urlparse(self.path).query
        self.wfile.write(f"GET request for {self.path}<br>".encode('utf-8'))

        if len(query_str) > 0:
            queries = [
                query_str] if "&" not in query_str else query_str.split("&")
            for qc in queries:
                key, val = qc.split("=")
                self.wfile.write(f"{key}: {val}<br>".encode('utf-8'))


def main(bind, port):
    """Run a http server."""
    logging.basicConfig(level=logging.INFO)
    httpd = HTTPServer((bind, port), RequestHandler)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


def parse_args():
    """Parse command-line arguments."""
    parser = ArgumentParser()
    parser.add_argument("--bind", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8888)
    return vars(parser.parse_args())


if __name__ == '__main__':
    main(**parse_args())
