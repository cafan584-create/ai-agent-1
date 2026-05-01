#!/bin/bash
# One-click deploy to Render.com
# Prerequisites: Render CLI installed (https://render.com/docs/cli)

echo "Deploying SOVEREIGN to Render..."

# Deploy web service from render.yaml
render deploy --config deploy/render.yaml

echo "Backend deployed! Now set these env vars in Render dashboard:"
echo "  - SUPABASE_DB_URL"
echo "  - FRED_API_KEY"
echo "  - EXCHANGERATE_API_KEY"
echo "  - TELEGRAM_BOT_TOKEN"
echo "  - GROQ_API_KEY"
echo ""
echo "Frontend: Push to Vercel or connect Git repo to Vercel for auto-deploy."
echo "Vercel config: deploy/vercel.json"
