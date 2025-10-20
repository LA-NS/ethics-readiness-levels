#!/bin/bash

# Version Switch Script for Ethics Readiness Levels Tool

case "$1" in
    "v0.1"|"stable"|"production")
        echo "🔄 Switching to V0.1 (Stable/Production)..."
        git checkout master
        echo "✅ Now on V0.1 - Production ready version"
        echo "📁 Version: $(cat VERSION)"
        ;;
    "v0.2"|"dev"|"development")
        echo "🔄 Switching to V0.2 (Development)..."
        git checkout v0.2-dev
        echo "✅ Now on V0.2 - Development version"
        echo "📁 Version: $(cat VERSION)"
        echo "⚠️  This is a development version - not for production use"
        ;;
    "status"|"info")
        echo "📊 Current Version Status:"
        echo "Branch: $(git branch --show-current)"
        echo "Version: $(cat VERSION)"
        echo "Last commit: $(git log -1 --pretty=format:'%h - %s')"
        echo ""
        echo "Available versions:"
        echo "  v0.1 (stable, production)"  
        echo "  v0.2 (development)"
        ;;
    *)
        echo "Ethics Readiness Levels Tool - Version Manager"
        echo "=============================================="
        echo ""
        echo "Usage: $0 [version]"
        echo ""
        echo "Available versions:"
        echo "  v0.1, stable, production    - Switch to stable V0.1"
        echo "  v0.2, dev, development      - Switch to development V0.2"
        echo "  status, info                - Show current status"
        echo ""
        echo "Examples:"
        echo "  $0 stable      # Switch to V0.1"
        echo "  $0 dev         # Switch to V0.2"
        echo "  $0 status      # Show current version"
        ;;
esac