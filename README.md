# Functional Resprites

민더스트리 v8 Build 159.7용 기능 중심 그래픽 모드의 레이어형 시제품입니다.

텍스처는 아틀라스 안정성을 위해 1x1 블록 기준 256픽셀로 저장되어 있습니다.
`texturescale: 0.125`를 사용해 바닐라 32픽셀 스프라이트와 같은 월드 크기로
표시합니다. 이 값은 이미지 해상도가 아니라 렌더링 배율입니다.

## 현재 적용

- `Drill 계열 전체`: 세르플로 드릴 4종, 에레키르 드릴·보어 4종과 빔 효과
- `Duo`: 받침은 단순화하고 좌우 포신을 크게 분리

바닐라 엔진이 드릴 회전, 포탑 조준·반동, 채굴·발사 이펙트를 계속 처리하도록
기존 스프라이트 레이어 이름을 유지했습니다.

## 설치

이 폴더를 압축하거나 폴더 그대로 Mindustry의 Mods 메뉴에서 가져옵니다.
게임이 설치된 뒤에는 `functional-resprites` 모드를 활성화하고 재시작합니다.

## 0.8.0 변경 사항

- Mechanical Drill과 Pneumatic Drill의 회전부를 다섯 겹의 얕은 나선 단차가
  이어지는 작은 원형 절삭면으로 다시 구성했습니다.
- 두 회전자 가장자리에는 회전해도 절삭 방향이 읽히는 작은 쐐기형 패드를
  분리했습니다. Mechanical은 황동, Pneumatic은 은회색 패드를 사용합니다.
- Laser Drill은 네 발사기와 굵은 보라색 빔을 하나의 회전 레이어에 유지하고,
  Blast Drill은 회전 방폭판과 고정된 용광로·가열 림을 분리해 기존 모션을
  보존합니다.

## 0.8.1 교정

- 승인 시안의 Mechanical·Pneumatic·Laser·Blast 회전자 실루엣을 실제
  `-rotator` 레이어에 맞춰 다시 분리했습니다. 시안의 나선 절삭면, 쐐기형
  절삭 패드, 네 방향 레이저 발사기, 방폭 세그먼트의 비율을 유지합니다.

## 0.8.2 교정

- 승인 시트의 8개 드릴·보어 베이스를 각각의 `<id>.png` 정적 레이어에
  적용했습니다. 중앙 개구부를 유지해 회전자, 아이템 마스크, 빔·글로우·화살표
  효과가 기존 순서대로 그려집니다.

## 0.7.0 변경 사항

- 세르플로의 `Mechanical Drill`, `Pneumatic Drill`, `Laser Drill`,
  `Blast Drill`을 승인된 기능 중심 디자인으로 완전히 다시 그렸습니다.
- 공통 외곽은 밝은 회색 금속 프레임과 제한된 명암 단계로 통일하되, 각 드릴의
  베이스와 회전 기구는 서로 다른 작동 방식을 드러내도록 구성했습니다.
- Mechanical Drill은 맞물리는 크기별 황동 기어열과 황동 절삭날이 솟은 원형
  나선 비트를 사용합니다.
- Pneumatic Drill은 밸브·굵은 호스가 연결된 은색 공기탱크와 나선 홈이 파인
  원형 압력 비트를 사용합니다.
- Laser Drill은 네 개의 포인터형 방사기와 굵은 보라색 광선 네 줄이 하나의
  회전 레이어로 움직입니다.
- Blast Drill은 용광로처럼 달아오른 내부 위에 다층 방폭판을 얹고, 붉은
  방폭벽 조각으로 이루어진 중앙 회전부를 사용합니다.
- 네 드릴의 광물 표시는 작은 육각형 마스크와 고정 테두리 안에 유지해 핵심
  기구를 가리지 않도록 했습니다.

## 0.6.0 변경 사항

- `Mechanical Drill`, `Pneumatic Drill`, `Laser Drill`, `Blast Drill`,
  `Plasma Bore`, `Large Plasma Bore`, `Impact Drill`, `Eruption Drill`을
  하나의 드릴 배치로 업그레이드했습니다.
- 외곽 실루엣, 중앙 기구, 색 배치와 각 건물의 고유 형태는 바닐라 원본을
  유지하고, 픽셀 계단을 정리한 각진 윤곽과 절제된 방향성 명암만 추가했습니다.
- 회전 드릴 헤드, 가열 림, 방향별 보어 상판, 빔·부스트 빔, 충격 드릴 화살표와
  반전 상판, 발광 레이어를 원래 파일 구조 그대로 분리했습니다.
- 크기별 공용 광물 마스크를 건드리지 않고 각 드릴 전용 `-item` 파일을 사용해
  다른 블록으로 변경 사항이 번지지 않도록 했습니다.

## 0.5.1 변경 사항

- 한 타일을 가득 채우는 전용 `duo-base`를 복원하고, 회전 상부의 폭을 약 80%로
  키워 받침 위에 작은 포탑이 올라간 것처럼 보이던 비율 문제를 수정했습니다.
- 바닐라 실루엣이 남을 수 있는 `duo-preview`, `duo-outline`, 좌우 포신의
  `-outline`까지 모두 커스텀 레이어로 교체했습니다.
- `duo-preview`는 새 본체와 두 포신을 합성한 중립 상태이므로 건설 미리보기와
  인게임 그림자도 새 실루엣을 사용합니다.
- 좌우 포신 파일과 반동 인덱스는 그대로 분리되어 번갈아 발사하는 모션을 유지합니다.

## 0.4.0 변경 사항

- 고해상도지만 매끈하고 제한된 색면을 사용하는 스타일로 재작업했습니다.
- 드릴 회전부는 기존 360도 회전 레이어를 유지합니다.
- 중앙 광물 표시는 실제 광물 이미지를 덮지 않고 작은 육각형 색상 마스크만 사용합니다.
- Duo 좌우 포신은 별도 레이어로 유지해 번갈아 발사하는 기본 반동을 보존합니다.

## 작업 원칙

새 건물처럼 재설계하지 않고 바닐라 실루엣과 팔레트를 기준으로 명암, 재질 구분,
기능부 가독성만 보강합니다. 모든 회전·발광·반동 모션은 기존 엔진이 처리합니다.

## 0.5.0 변경 사항

- Build 159.7 레이어 참조에 따라 첫 재구성 배치를 적용했습니다.
- Mechanical Drill은 `mechanical-drill`, `-rotator`, `-top`,
  `-item`의 네 레이어를 분리했습니다. 광물 색상은 전용 `-item` 마스크에만
  런타임 틴트되므로 다른 2x2 드릴에는 영향을 주지 않습니다.
- Duo는 당시 개별 `duo-base` 덮어쓰기를 제거하고 회전 본체와 좌우 독립 반동
  포신만 교체했으나, 이 방식은 바닐라 받침과 생성 레이어가 너무 강하게 남는
  문제가 있어 0.5.1에서 다시 수정했습니다.
- 모든 신규 형태는 바닐라의 회색·갈색 팔레트, 탑뷰 피벗, 정상 확대 배율의
  식별성을 우선했습니다.

## 0.4.4 변경 사항

- Duo 포신을 세워진 원통처럼 보이는 형태에서, 전방으로 평행하게 뻗는 평면형
  이중 자동포로 다시 그렸습니다.
- 총구는 작은 사각 개구부로 처리해 탑뷰에서도 발사 방향이 즉시 읽히도록 했습니다.

## 0.4.3 변경 사항

- Duo 받침을 저대비의 얇은 지지 프레임으로 다시 만들고, 포탑 본체를 총열이
  가려지지 않는 열린 회전 프레임으로 변경했습니다.
- 좌우 총열을 10% 키우고 투명 여백을 유지해, 본체 아래에 그려져도 총구와
  총열이 선명하게 보이도록 조정했습니다.

## 0.4.2 변경 사항

- Duo의 렌더 레이어를 실제 엔진 구조에 맞게 `duo-base.png`, `duo.png`,
  `duo-barrel-l/r.png`로 분리했습니다.
- `duo.png`에는 회전하는 포탑 본체만 넣고, 좌우 포신은 별도 이미지로 유지해
  원본 듀오가 바탕에 남는 문제를 해결했습니다.

## 0.4.1 변경 사항

- Duo 본체에서 포신처럼 보이는 중앙 구조를 제거했습니다.
- 좌우 포신이 본체 위에 겹쳐 보이지 않고 독립적으로 보이도록 받침을 정리했습니다.
- 드릴 중앙 광물 색상 마스크에 어두운 외곽선과 밝은 내부 테두리를 추가했습니다.

## 0.2.4 변경 사항

- 고해상도 스프라이트가 맵 전체를 덮던 렌더링 배율 오류를 수정했습니다.
- 1x1인 Duo는 256x256, 2x2인 Mechanical Drill은 512x512로 저장해
  블록 크기별 표시 크기를 맞췄습니다.

## 0.2.5 변경 사항

- `drill-item-2.png`를 교체해 Mechanical Drill 중앙의 광물 표시를
  단순한 색상 마커 대신 입체 결정체로 변경했습니다.
- 게임이 현재 채굴 중인 광물의 색으로 이 레이어를 자동 틴트하므로,
  광물 종류별 색상과 기존 채굴 판정은 그대로 유지됩니다.

## 0.2.6 변경 사항

- 광물 결정체를 1x1 블록 안쪽 크기로 줄여 드릴 본체와 회전부를 가리지 않도록
  조정했습니다.
Functional Resprites 0.8.4

This version retains the four Serpulo drill mechanisms and refines the two
mechanical cutters with stepped five-groove spiral faces and distinct cutter pads.

- All eight Build 159.7 drill and bore blocks now use vanilla-faithful 8x
  resprites with smoother angular contours and restrained directional shading.
- Rotators, tops, mined-item masks, heat rims, directional bore emitters, beams,
  progress arrows, inversion plates, and additive glows remain separate runtime
  layers, preserving every original animation.
- The same `item-*.png` files override the vanilla item regions, so conveyor
  items and item UI use matching copper, lead, coal, and Erekir material shapes.
- Duo replaces the complete visible render stack: its static `duo-base.png`,
  rotating `duo.png`, neutral `duo-preview.png`, body and barrel outlines, and
  the two flat forward-facing `duo-barrel-l/r.png` recoil layers.
- The rotating upper assembly now fills roughly 80% of the tile width instead
  of appearing as a small attachment over a vanilla-sized foundation.
- The vanilla alternate-fire and per-barrel recoil behavior are intentionally
  preserved while every visible Duo layer is replaced.

### 0.8.4

- Removed the four detached grey clamp blocks from each conventional drill's
  fixed top layer. The top layer now contains only the small central collar,
  leaving the mechanism visible.

### 0.8.3

- Mechanical, Pneumatic, and Laser Drill `-top` layers now use fixed angular
  retaining collars instead of circular overlays, so their rotating mechanisms
  remain unobscured while the center reads as a protected drill opening.
- The four Serpulo drill `-item` masks are now smaller, faceted ore fragments.
  Mindustry still tints them from the mined item at runtime; the fixed collar
  supplies the dark border without covering the drill face.
- The Blast Drill's existing separated furnace rim and reinforced top layer are
  retained, preserving its additive heat animation.

The package is a texture-only override for vanilla blocks; no block behavior,
recipes, save data, or campaign data are changed.

Remove older `functional-resprites` copies from the Mindustry Mods folder before
installing this version, so duplicate atlas overrides cannot remain enabled.
