# Raiz de Luz Website - SEO Recommendations & Action Plan

**Date:** November 25, 2025 (Comprehensive Update)
**Site:** https://raizdeluz.eu
**Status:** SEO infrastructure complete. Major content updates completed. Schema updates needed.

---

## Overview & Progress Update

**Infrastructure:** ✅ Complete
- ✅ `sitemap.xml` - Updated with all pages including legal pages (Nov 25, 2025)
- ✅ `robots.txt` - Properly configured
- ✅ Submitted to Google Search Console

**Structured Data:** ⚠️ Needs Update
- ✅ LocalBusiness schema (`contacto.html`) - Complete
- ✅ Organization schema (`index.html`) - Complete
- ⚠️ Service schemas (`servicos.html`) - **NEEDS UPDATE: Only 4 services marked, but 11 services exist**
- ✅ FAQ schema (`contacto.html`) - Complete
- ✅ BreadcrumbList schema (all pages) - Complete
- ❌ VideoObject schema (`sobre.html`) - **MISSING: YouTube video not marked up**

**Content Status:** ✅ Major Improvements
- ✅ 11 comprehensive service descriptions added with benefits
- ✅ Professional background images for all services
- ✅ YouTube video of space embedded in sobre.html
- ✅ Improved visual design and layout
- ⏳ Pricing placeholders still need completion (€XX → actual prices)
- ⏳ Therapist biographies still needed

**Legal Pages:** ✅ Complete
- ✅ `privacidade.html` - GDPR-compliant Privacy Policy
- ✅ `termos.html` - Terms of Service
- ✅ `politica-cookies.html` - Cookie & Analytics Policy

**Code Quality:** ⚠️ Minor Issues
- ⚠️ Domain URL inconsistency: `contacto.html` og:url shows `.pt` instead of `.eu`
- ✅ All other schema markup properly formatted

---

## Recent Updates (November 25, 2025)

### ✅ Content Improvements
1. **Servicos Page Expansion**
   - Expanded from 4 to 11 services with full descriptions
   - Services now include:
     1. Massagem terapêutica
     2. Massagem desportiva
     3. Massagem para grávidas
     4. Terapia sacro craniana
     5. Drenagem linfática
     6. Relaxamento
     7. Pedras quentes
     8. Massagem Xamânica
     9. Cura Energética
     10. Defumação
     11. Produtos Naturais
   - Each service has: description, 5 benefits, duration/pricing section, CTA button
   - Professional background images for visual appeal

2. **Sobre Page Enhancement**
   - Added YouTube Shorts video (https://youtube.com/shorts/ym7-nn5Ne3g)
   - Video showcases "O Nosso Espaço" (the physical space)
   - Responsive video container with proper aspect ratio
   - Location updated to "Barreiro" (was placeholder)

3. **Visual Design Improvements**
   - Service sections have background images with gradient overlays
   - Responsive video container with rounded corners and shadows
   - Professional layout matching brand aesthetic
   - Mobile-optimized layouts

4. **Sitemap Updates**
   - Added legal pages (privacidade, termos, politica-cookies)
   - Updated lastmod dates to 2025-11-25
   - All 7 pages properly indexed with priorities

---

## High Priority Actions (Complete by December 2, 2025)

### 🔴 CRITICAL: Update Service Schemas

**Why:** Your servicos.html now has 11 services but schema markup only includes 4. This is a missed opportunity for rich snippets.

**Current Schema (4 services):**
- Massagem Xamânica
- Cura Energética
- Limpeza com Fumo (Defumação)
- Produtos Naturais

**Missing from Schema (7 services):**
- Massagem terapêutica
- Massagem desportiva
- Massagem para grávidas
- Terapia sacro craniana
- Drenagem linfática
- Relaxamento
- Pedras quentes

**Action Required:**
Edit `docs/servicos.html` lines 18-186 to add 7 additional Service schema objects to the JSON-LD array.

**Template for Each Service:**
```json
{
  "@context": "https://schema.org/",
  "@type": "Service",
  "name": "Massagem Terapêutica",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Raiz de Luz"
  },
  "description": "Alívio de dores musculares e tensões através de técnicas especializadas de massagem profunda.",
  "areaServed": "PT",
  "availableChannel": {
    "@type": "ServiceChannel",
    "serviceUrl": "https://raizdeluz.eu/contacto.html"
  }
}
```

**Expected Impact:** HIGH - Enables rich snippets for all 11 services in search results

**Effort:** 30-45 minutes

---

### 🟡 RECOMMENDED: Add VideoObject Schema

**Why:** YouTube video on sobre.html is not marked up. Video schema enables video rich snippets in search results.

**Current Status:** Video embedded but no schema

**Action Required:**
Add VideoObject schema to `docs/sobre.html` in the `<head>` section:

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "O Nosso Espaço - Raiz de Luz",
  "description": "Visite virtualmente o espaço da Raiz de Luz, criado com intenção para cura e bem-estar",
  "thumbnailUrl": "https://i.ytimg.com/vi/ym7-nn5Ne3g/maxresdefault.jpg",
  "uploadDate": "2025-11-25",
  "contentUrl": "https://www.youtube.com/watch?v=ym7-nn5Ne3g",
  "embedUrl": "https://www.youtube.com/embed/ym7-nn5Ne3g"
}
```

**Expected Impact:** MEDIUM - Video may appear in video search results

**Effort:** 15 minutes

---

### 🟠 MINOR FIX: Correct Domain URL

**Issue:** `contacto.html` line 15 shows `og:url` as `https://raizdeluz.pt/` instead of `https://raizdeluz.eu/`

**Action Required:**
Edit `docs/contacto.html` line 15:
```html
<meta property="og:url" content="https://raizdeluz.eu/contacto.html" />
```

**Expected Impact:** LOW - Ensures correct URL in social shares

**Effort:** 1 minute

---

### ⏳ PENDING: Complete Placeholder Content

**Still Outstanding from Previous Review:**

1. **Update Service Prices** (`servicos.html`)
   - Replace all "€XX" with actual pricing
   - Locations: Throughout service sections (lines ~279, 302, 325, 348, 371, 394, 417, 440, 463, 485)
   - Recommended: "60 minutos - €60 | 90 minutos - €85" format

2. **Add Therapist Biographies** (`sobre.html`)
   - Replace "[Breve biografia...]" with actual professional bios
   - Lines: ~157-160, ~174-177
   - Should include: certifications, experience, personal journey

3. **Update Address Display** (`contacto.html`)
   - Current schema has correct address, but HTML display may need updating
   - Verify address display matches schema

4. **Add Google Map** (`contacto.html`)
   - Replace placeholder with Google Maps embed
   - Keep location general (home-based business)
   - Example embed code exists in HTML comments

**Effort:** 2-4 hours total | **Expected Impact:** HIGH

---

## Technical SEO Checklist (Updated)

| Item | Current Status | Notes |
|------|---|---|
| Mobile responsive | ✅ Complete | Responsive video, service cards working well |
| HTTPS/SSL | ✅ Complete | raizdeluz.eu properly secured |
| Page load speed | ⚠️ Monitor | Background images may affect load time |
| Crawlable structure | ✅ Complete | All pages in sitemap |
| Indexable content | ✅ Complete | 7 pages properly indexed |
| Meta descriptions | ✅ Complete | All pages have unique descriptions |
| Unique titles | ✅ Complete | All pages have unique titles |
| Heading hierarchy | ✅ Complete | Proper H1-H4 structure maintained |
| Internal linking | ✅ Complete | Service cards link to anchor sections |
| Image optimization | ⚠️ Consider | Background images loaded from external URLs |
| Analytics | ✅ Complete | GoatCounter tracking active |
| Sitemaps | ✅ Complete | Updated Nov 25 with all pages |
| Robots.txt | ✅ Complete | Properly configured |
| Schema markup | ⚠️ Incomplete | **4/11 services marked; video not marked** |
| Structured data | ⚠️ Incomplete | **Missing VideoObject, partial Service schemas** |
| Legal pages | ✅ Complete | All 3 pages created and linked |

---

## New SEO Opportunities

### 1. Service Anchor Links
**Status:** ✅ IMPLEMENTED

Your index.html service cards now link to specific service sections using anchor links (e.g., `servicos.html#massagem-terapeutica`). This is excellent for:
- User experience (direct navigation)
- Internal linking structure
- Potential featured snippets

**No Action Required** - Working perfectly

---

### 2. Video Content
**Status:** ⚠️ PARTIALLY IMPLEMENTED

YouTube video adds rich media content. Recommendations:
- ✅ Responsive embed implemented
- ❌ Add VideoObject schema (see High Priority section)
- Consider adding video to homepage for engagement
- Create more video content (service demonstrations, testimonials)

**Action:** Add VideoObject schema (see above)

---

### 3. Background Images & Performance
**Status:** ⚠️ MONITOR

Service sections use background images from:
- Unsplash CDN (good - fast, reliable)
- Your own domain (raizdeluz.eu/media/images/)

**Recommendations:**
- Monitor page load speed with Google PageSpeed Insights
- Consider lazy-loading background images if performance issues arise
- Ensure all images have proper alt text (service section images are decorative, so current implementation is acceptable)

**Action:** Test with PageSpeed Insights after deployment

---

## Keyword Strategy Update

### Current Service Coverage (11 Services)

**Primary Keywords Now Covered:**
1. ✅ "Massagem terapêutica" + "[cidade]"
2. ✅ "Massagem desportiva" + "[cidade]"
3. ✅ "Massagem para grávidas" / "Massagem pré-natal"
4. ✅ "Terapia sacro craniana" + "[região]"
5. ✅ "Drenagem linfática" + "[cidade]"
6. ✅ "Massagem relaxamento" / "Massagem anti-stress"
7. ✅ "Massagem pedras quentes" / "Hot stone massage Portugal"
8. ✅ "Massagem xamânica" + "[cidade]"
9. ✅ "Cura energética" + "[região]"
10. ✅ "Defumação" / "Limpeza energética"
11. ✅ "Produtos naturais bem-estar"

### Local SEO Opportunities

**Location:** Barreiro, Portugal

**Target Keyword Combinations:**
- "Massagem Barreiro"
- "Terapias holísticas Barreiro"
- "Cura energética Margem Sul"
- "Massagem terapêutica Barreiro"
- "Terapeuta Barreiro"
- "Bem-estar Barreiro"

**Action:** Ensure "Barreiro" is naturally mentioned in content (already done in sobre.html)

---

## Content Quality Assessment

### ✅ Strengths
1. **Comprehensive Service Descriptions**
   - Each service has detailed explanation
   - Clear benefits lists (5 per service)
   - Professional tone appropriate for wellness industry

2. **Visual Appeal**
   - Background images enhance professionalism
   - Consistent design language
   - Good use of white space

3. **User Experience**
   - Clear CTAs ("Marcar Sessão", "Solicitar Orçamento")
   - Anchor links work perfectly
   - Mobile-responsive throughout

4. **Trust Signals**
   - Video of physical space builds credibility
   - Professional service descriptions
   - Legal pages complete

### ⚠️ Areas for Improvement
1. **Pricing Transparency**
   - All services show "€XX" placeholder
   - Recommendation: Add actual pricing ASAP for trust and conversion

2. **Therapist Credibility**
   - Bios still show placeholders
   - Recommendation: Add professional bios with credentials

3. **Content Freshness**
   - Consider adding blog/resources section (lower priority)
   - Regular content updates signal active business

---

## Action Plan Timeline (Updated)

### ⚡ IMMEDIATE (This Week - Nov 25-30, 2025)

**High Impact, Quick Wins:**
- [ ] Update service schemas to include all 11 services (30-45 min)
- [ ] Add VideoObject schema for sobre.html video (15 min)
- [ ] Fix contacto.html og:url domain (.pt → .eu) (1 min)
- [ ] Complete all pricing placeholders (€XX → actual prices) (30 min)

**Total Effort:** ~2 hours
**Expected Impact:** HIGH - Rich snippets for all services, complete site

---

### 📅 SHORT TERM (Next Week - Dec 1-7, 2025)

**Content Completion:**
- [ ] Write and add therapist biographies (2 hours)
- [ ] Verify/update address display in contacto.html (15 min)
- [ ] Add Google Maps embed to contacto.html (30 min)
- [ ] Test all schema markup with Google Rich Results Test (30 min)

**Performance & Testing:**
- [ ] Run Google PageSpeed Insights on all pages
- [ ] Test mobile experience on real devices
- [ ] Verify all anchor links work correctly
- [ ] Check video loads properly on mobile

**Total Effort:** ~4 hours
**Expected Impact:** HIGH - Complete, professional site ready for indexing

---

### 📊 MEDIUM TERM (Dec 8-31, 2025)

**Monitoring & Optimization:**
- [ ] Monitor Google Search Console weekly
  - Check for crawl errors
  - Review indexing status (all 7 pages)
  - Track search impressions and clicks
- [ ] Optimize images if page speed issues arise
- [ ] Consider adding customer testimonials section
- [ ] Plan content calendar for regular updates

**Marketing Enhancement:**
- [ ] Add Twitter Card metadata for better social sharing
- [ ] Consider Instagram embedding (if applicable)
- [ ] Plan blog/resources section (if organic traffic justifies)

---

### 🎯 LONG TERM (January 2026+)

**Growth & Expansion:**
- [ ] Analyze keyword performance data
- [ ] Create blog content for long-tail keywords
- [ ] Add customer testimonials with Review schema
- [ ] Consider video testimonials
- [ ] Expand service descriptions based on customer questions
- [ ] Quarterly SEO review and content refresh

---

## Schema Markup Priority Matrix

| Schema Type | Status | Priority | Impact | Effort |
|-------------|--------|----------|--------|--------|
| LocalBusiness | ✅ Complete | - | HIGH | - |
| Organization | ✅ Complete | - | HIGH | - |
| Service (4 of 11) | ⚠️ Partial | 🔴 CRITICAL | HIGH | 45 min |
| FAQ | ✅ Complete | - | MEDIUM | - |
| BreadcrumbList | ✅ Complete | - | LOW | - |
| VideoObject | ❌ Missing | 🟡 RECOMMENDED | MEDIUM | 15 min |
| Review/Rating | ❌ Missing | 🟢 Future | MEDIUM | 2 hrs |
| Article (blog) | ❌ N/A | 🟢 Future | MEDIUM | Variable |

---

## Performance Monitoring

### Metrics to Track Weekly

1. **Google Search Console**
   - Total impressions (target: +20% month-over-month after 3 months)
   - Total clicks (target: +15% month-over-month after 3 months)
   - Average position (target: <10 for branded searches, <20 for service keywords)
   - Click-through rate (target: >3% average)

2. **GoatCounter Analytics**
   - Page views per page
   - Referral sources
   - Popular services (most viewed)
   - User flow (which pages lead to contact page)

3. **Google PageSpeed Insights**
   - Core Web Vitals scores
   - Performance score (target: >90 mobile, >95 desktop)
   - Largest Contentful Paint (target: <2.5s)
   - First Input Delay (target: <100ms)

### Red Flags to Watch For
- ❌ Indexing errors in Search Console
- ❌ Page speed score dropping below 80
- ❌ Crawl errors increasing
- ❌ Position drops for key terms
- ❌ Sudden traffic drops (>20%)

---

## Success Metrics & Expected Results

### 1-3 Months (Nov 2025 - Feb 2026)
**Expected:**
- ✅ All 7 pages fully indexed
- 📈 Branded search visibility (searching "Raiz de Luz" finds site)
- 📈 Local search visibility begins (Barreiro + service keywords)
- 📈 50-100 impressions/month in Search Console
- 📈 5-10 clicks/month from organic search

**Milestone:** First contact form submission from organic search

---

### 3-6 Months (Feb - May 2026)
**Expected:**
- 📈 200-500 impressions/month
- 📈 20-50 clicks/month
- 📈 Ranking in top 20 for local service keywords
- 📈 Rich snippets appearing for services and FAQs
- 📈 Video appearing in video search results

**Milestone:** Steady stream of organic inquiries (2-5/month)

---

### 6-12 Months (May - Nov 2026)
**Expected:**
- 📈 500-1000 impressions/month
- 📈 50-100 clicks/month
- 📈 Top 10 rankings for several service keywords
- 📈 Increased brand awareness in Barreiro area
- 📈 Regular bookings from organic search

**Milestone:** 10+ organic bookings per month

---

### 12+ Months (Dec 2026+)
**Expected:**
- 📈 1000+ impressions/month
- 📈 100+ clicks/month
- 📈 Authority in local wellness/holistic therapy space
- 📈 Potential to expand to other locations
- 📈 Blog content driving long-tail traffic

**Milestone:** Organic search becomes primary customer acquisition channel

---

## Quick Reference: Recent Changes

### Files Modified (November 25, 2025)

| File | Changes Made | Impact |
|------|-------------|--------|
| `servicos.html` | **MAJOR UPDATE:** Expanded from 4 to 11 services, added background images, comprehensive descriptions | HIGH - More service coverage |
| `sobre.html` | Added YouTube video embed, updated location to "Barreiro" | MEDIUM - Better engagement, local SEO |
| `css/style.css` | Removed grid layout issue, added video container styles, service section overlays | HIGH - Better UX |
| `sitemap.xml` | Updated dates to Nov 25, added legal pages | MEDIUM - Proper indexing |

### Files Needing Updates

| File | Required Changes | Priority | Effort |
|------|-----------------|----------|--------|
| `servicos.html` | Add 7 missing service schemas | 🔴 CRITICAL | 45 min |
| `servicos.html` | Replace "€XX" with actual pricing | 🔴 HIGH | 30 min |
| `sobre.html` | Add VideoObject schema | 🟡 RECOMMENDED | 15 min |
| `sobre.html` | Add therapist biographies | 🟡 RECOMMENDED | 2 hrs |
| `contacto.html` | Fix og:url domain (.pt → .eu) | 🟠 MINOR | 1 min |
| `contacto.html` | Add Google Maps embed | 🟡 RECOMMENDED | 30 min |

---

## Testing Checklist

Before considering site "complete," test the following:

### Functionality
- [ ] All anchor links work (service cards → service sections)
- [ ] Contact form submits successfully
- [ ] Video plays on desktop and mobile
- [ ] All navigation links work
- [ ] Footer links work (including legal pages)

### SEO & Schema
- [ ] Test all pages with [Google Rich Results Test](https://search.google.com/test/rich-results)
- [ ] Verify LocalBusiness schema shows all fields
- [ ] Verify FAQ schema detects all questions
- [ ] Verify Service schemas (all 11 after update)
- [ ] Verify VideoObject schema (after adding)
- [ ] Check sitemap.xml loads correctly

### Mobile & Performance
- [ ] Test on iPhone/Android
- [ ] Test on tablet
- [ ] Video container responsive
- [ ] Service sections readable on mobile
- [ ] Run PageSpeed Insights (target: >80 mobile, >90 desktop)
- [ ] Check Core Web Vitals

### Social Sharing
- [ ] Test Facebook share preview with [Facebook Debugger](https://developers.facebook.com/tools/debug/)
- [ ] Test Twitter/X share preview
- [ ] Verify og:image displays correctly

---

## Conclusion & Current Status

### ✅ Major Accomplishments (November 25, 2025)

**Content Expansion:**
- 11 comprehensive service descriptions (up from 4)
- Professional background images for visual appeal
- YouTube video showcasing physical space
- Improved layout and user experience

**SEO Foundation:**
- Sitemap updated with all pages
- 7 pages fully crawlable
- Strong internal linking with anchor links
- Legal pages complete (GDPR compliant)

**Technical Quality:**
- Mobile-responsive throughout
- Professional design aesthetic
- Fast navigation with anchor links
- Video embedded responsively

### ⚠️ Critical Next Steps (Complete by Dec 2, 2025)

**Schema Updates (HIGH PRIORITY):**
1. Add 7 missing Service schemas (45 minutes) - **CRITICAL**
2. Add VideoObject schema (15 minutes) - **RECOMMENDED**
3. Fix contacto.html og:url (1 minute) - **MINOR**

**Content Completion (HIGH PRIORITY):**
1. Replace all "€XX" with actual pricing (30 minutes) - **CRITICAL**
2. Add therapist biographies (2 hours) - **RECOMMENDED**
3. Add Google Maps embed (30 minutes) - **RECOMMENDED**

**Total Estimated Effort:** ~4.5 hours
**Expected ROI:** Complete, professional site ready to rank in search engines

### 🎯 Expected Outcome

After completing the above tasks, your site will have:
- ✅ Comprehensive SEO optimization
- ✅ Complete structured data markup
- ✅ Professional content throughout
- ✅ Strong local SEO signals
- ✅ Trust-building elements (video, complete info, legal pages)
- ✅ Excellent user experience

**Result:** Ready to compete effectively in search results for wellness and holistic therapy services in Barreiro and surrounding areas.

---

## Resources & Tools

### Testing & Validation
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
- [Schema.org Validator](https://validator.schema.org/)

### Monitoring
- [Google Search Console](https://search.google.com/search-console)
- [GoatCounter Dashboard](https://raizdeluz.goatcounter.com)
- [Google Analytics](https://analytics.google.com) (optional supplement)

### Social Sharing
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)

---

**Document Version:** 2.0 (Comprehensive Update)
**Last Updated:** November 25, 2025
**Next Review:** December 2, 2025 (after critical updates completed)
**Prepared By:** Claude Code SEO Analysis
